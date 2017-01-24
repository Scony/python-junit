import xml.etree.ElementTree as ET
import xml.dom.minidom as MD


class TestReport(object):


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

            timesInSuites = [anything2float(ts.params['time']) for ts in testSuites]
            timesInSuites = [time for time in timesInSuites if time is not None]
            self.params['time'] = self.params['timeAggregate'](timesInSuites)

            testsInSuites = [anything2int(ts.params['tests']) for ts in testSuites]
            testsInSuites = [tests for tests in testsInSuites if tests is not None]
            self.params['tests'] = sum(testsInSuites)

            failuresInSuites = [anything2int(ts.params['failures']) for ts in testSuites]
            failuresInSuites = [failures for failures in failuresInSuites if failures is not None]
            self.params['failures'] = sum(failuresInSuites)

            errorsInSuites = [anything2int(ts.params['errors']) for ts in testSuites]
            errorsInSuites = [errors for errors in errorsInSuites if errors is not None]
            self.params['errors'] = sum(errorsInSuites)

            self.params['testSuites'] = testSuites

        self.params.update(kwargs)


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
        raise NotImplementedError


    def merge(self, testReport):
        raise NotImplementedError


    def __str__(self):
        return str(self.params)
