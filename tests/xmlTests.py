import unittest
import re

import junit


class TestXmlCoding(unittest.TestCase):

    def testSimpleEncoding1(self):
        tr = junit.TestReport(name='xyz')
        xml = tr.toXml()
        xml = xml.decode('utf-8')
        self.assertEqual('<testsuites' in xml, True)
        self.assertEqual('name="xyz"' in xml, True)

    def testSimpleEncoding2(self):
        tr = junit.TestReport(name='xyz')
        xml = tr.toXml()
        xml = xml.decode('utf-8')
        self.assertEqual('<testsuites' in xml, True)
        self.assertEqual('name="xyz"' in xml, True)
        self.assertEqual('time="' not in xml, True)
        self.assertEqual('tests="' not in xml, True)
        self.assertEqual('errors="' not in xml, True)

    def testSimpleEncoding3(self):
        tr = junit.TestReport(name='xyz',
                              time=1.1,
                              tests=5,
                              errors='24')
        xml = tr.toXml()
        xml = xml.decode('utf-8')
        self.assertEqual('<testsuites' in xml, True)
        self.assertEqual('name="xyz"' in xml, True)
        self.assertEqual('time="1.1' in xml, True)
        self.assertEqual('tests="5"' in xml, True)
        self.assertEqual('errors="24"' in xml, True)

    def testCompoundEncoding1(self):
        tss = [junit.TestSuite() for _ in range(3)]
        tr = junit.TestReport(tss, name='xyz')
        xml = tr.toXml()
        xml = xml.decode('utf-8')
        self.assertEqual('<testsuites' in xml, True)
        self.assertEqual('name="xyz"' in xml, True)
        self.assertEqual(len(re.findall('<testsuite ', xml)), 3)

    def testCompoundEncoding2(self):
        tr = junit.TestReport([
            junit.TestSuite(name='aaa', errors=5),
            junit.TestSuite(name='bbb', skipped=7),
            junit.TestSuite(name='ccc', time=21),
        ], name='xyz')
        xml = tr.toXml()
        xml = xml.decode('utf-8')
        self.assertEqual('<testsuites' in xml, True)
        self.assertEqual('name="xyz"' in xml, True)
        self.assertEqual('name="aaa"' in xml, True)
        self.assertEqual('name="bbb"' in xml, True)
        self.assertEqual('name="ccc"' in xml, True)
        self.assertEqual('errors="5"' in xml, True)
        self.assertEqual('skipped="7"' in xml, True)
        self.assertEqual('time="21' in xml, True)
        self.assertEqual(len(re.findall('<testsuite ', xml)), 3)

    def testCompoundEncoding3(self):
        tr = junit.TestReport([
            junit.TestSuite(tests=5, time='1.1'),
            junit.TestSuite(tests=7, time=7),
            junit.TestSuite(time=10),
        ], name='xyz')
        xml = tr.toXml()
        xml = xml.decode('utf-8')
        self.assertEqual('<testsuites' in xml, True)
        self.assertEqual('name="xyz"' in xml, True)
        self.assertEqual('tests="5"' in xml, True)
        self.assertEqual('tests="7"' in xml, True)
        self.assertEqual('tests="12"' in xml, True)
        self.assertEqual('time="1.1' in xml, True)
        self.assertEqual('time="7' in xml, True)
        self.assertEqual('time="10' in xml, True)
        self.assertEqual('time="18.1' in xml, True)
        self.assertEqual(len(re.findall('<testsuite ', xml)), 3)

    def testComplexEncoding1(self):
        tr = junit.TestReport([
            junit.TestSuite([
                junit.TestCase(),
                junit.TestCase(),
            ]),
            junit.TestSuite([
                junit.TestCase(),
                junit.TestCase(),
            ]),
        ], name='xyz')
        xml = tr.toXml()
        xml = xml.decode('utf-8')
        self.assertEqual('<testsuites' in xml, True)
        self.assertEqual('name="xyz"' in xml, True)
        self.assertEqual(len(re.findall('<testsuite ', xml)), 2)
        self.assertEqual(len(re.findall('<testcase ', xml)), 4)


if __name__ == '__main__':
    unittest.main()
