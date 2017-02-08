import xml.etree.ElementTree as ET
import xml.dom.minidom as MD

from .testSuite import TestSuite
from .testCase import TestCase


class TestReport(object):


    class XmlDecodingFailure(Exception):
        pass


    def __init__(self, testSuites=None, **kwargs):
        self.params = {
            'time': None,
            'name': None,
            'tests': None,
            'failures': None,
            'errors': None,
            'disabled': None,
            'testSuites': [],
            'timeAggregate': sum,
        }
        self.attributeNames = [
            'time',
            'name',
            'tests',
            'failures',
            'errors',
            'disabled',
        ]

        if 'timeAggregate' in kwargs and kwargs['timeAggregate'] is not None:
            self.params['timeAggregate'] = kwargs['timeAggregate']

        if testSuites is not None and not isinstance(testSuites, list):
            testSuites = [testSuites]

        if testSuites is not None:
            self.params['testSuites'] = testSuites
            self._recalculateParams()

        self.params.update(kwargs)


    def toRawData(self):
        testReportData = {
            'testSuites': [],
        }

        for testSuite in self.params['testSuites']:
            testSuiteData = {
                'testCases': [],
            }

            for testCase in testSuite.params['testCases']:
                testSuiteData['testCases'].append(testCase.params)

            testSuiteData.update(dict([(k, v) for k, v in testSuite.params.items() if
                                       k in testSuite.attributeNames]))
            testReportData['testSuites'].append(testSuiteData)

        testReportData.update(dict([(k, v) for k, v in self.params.items() if k in self.attributeNames]))

        return testReportData


    def toXml(self, prettyPrint=False):
        testsuitesAttrib = dict([(key, str(val)) for key, val in self.params.items() if
                                 key in self.attributeNames and
                                 val is not None])
        testsuitesNode = ET.Element('testsuites', attrib=testsuitesAttrib)
        for testSuite in self.params['testSuites']:
            testsuiteAttrib = dict([(key, str(val)) for key, val in testSuite.params.items() if
                                    key in testSuite.attributeNames and
                                    val is not None])
            testsuiteNode = ET.SubElement(testsuitesNode, 'testsuite', attrib=testsuiteAttrib)
            for testCase in testSuite.params['testCases']:
                testcaseAttrib = dict([(key, str(val)) for key, val in testCase.params.items() if
                                       key in testCase.attributeNames and
                                       val is not None])
                testcaseNode = ET.SubElement(testsuiteNode, 'testcase', attrib=testcaseAttrib)
                for childName in testCase.childNames.keys():
                    childAttrib = dict([(key.split('_')[1], str(val)) for key, val in testCase.params.items() if
                                        key.startswith('%s_' % childName) and
                                        val is not None])
                    if testCase.params[childName] is not None or len(childAttrib.items()) > 0:
                        childNode = ET.SubElement(testcaseNode, testCase.childNames[childName], attrib=childAttrib)
                        childNode.text = str(testCase.params[childName])

        uglyXml = ET.tostring(testsuitesNode, encoding='utf8')

        if prettyPrint:
            xml = MD.parseString(uglyXml)
            return xml.toprettyxml()

        return uglyXml


    def fromXml(self, xmlStr):
        self._clearAttributes()

        root = ET.fromstring(xmlStr)
        if root.tag != 'testsuites':
            raise self.XmlDecodingFailure

        self._fillAttributes(root.attrib)
        self.params['testSuites'] = []

        for child in root:
            if child.tag == 'testsuite':
                testSuite = TestSuite()
                testSuite._fillAttributes(child.attrib)

                for subchild in child:
                    if subchild.tag == 'testcase':
                        testCase = TestCase()
                        testCase._fillAttributes(subchild.attrib)

                        for subsubchild in subchild:
                            if subsubchild.tag in testCase.childNames.values():
                                childNamesToParamNames = dict([(v, k) for k, v in testCase.childNames.items()])
                                paramName = childNamesToParamNames[subsubchild.tag]
                                testCase.params[paramName] = subsubchild.text
                                for attributeName, attributeValue in subsubchild.attrib.items():
                                    testCase.params['%s_%s' % (paramName, attributeName)] = attributeValue

                        testSuite.params['testCases'].append(testCase)

                testSuite._recalculateParams()
                self.params['testSuites'].append(testSuite)

        self._recalculateParams()


    def merge(self, testReport):
        raise NotImplementedError


    def __str__(self):
        return str(self.params)


    def _clearAttributes(self):
        for attributeName in self.attributeNames:
            self.params[attributeName] = None


    def _fillAttributes(self, attributes):
        for attributeName in self.attributeNames:
            if attributeName in attributes:
                self.params[attributeName] = attributes[attributeName]


    def _recalculateParams(self):
        def anything2int(anything):
            try:
                return int(anything)
            except:
                return None

        def anything2float(anything):
            try:
                return float(anything)
            except:
                return None

        timesInSuites = [anything2float(ts.params['time']) for ts in self.params['testSuites']]
        timesInSuites = [time for time in timesInSuites if time is not None]
        self.params['time'] = self.params['timeAggregate'](timesInSuites)

        testsInSuites = [anything2int(ts.params['tests']) for ts in self.params['testSuites']]
        testsInSuites = [tests for tests in testsInSuites if tests is not None]
        self.params['tests'] = sum(testsInSuites)

        failuresInSuites = [anything2int(ts.params['failures']) for ts in self.params['testSuites']]
        failuresInSuites = [failures for failures in failuresInSuites if failures is not None]
        self.params['failures'] = sum(failuresInSuites)

        errorsInSuites = [anything2int(ts.params['errors']) for ts in self.params['testSuites']]
        errorsInSuites = [errors for errors in errorsInSuites if errors is not None]
        self.params['errors'] = sum(errorsInSuites)
