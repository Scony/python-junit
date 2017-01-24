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

    def testComplexEncoding2(self):
        tr = junit.TestReport([
            junit.TestSuite([
                junit.TestCase(name='tc1'),
                junit.TestCase(name='tc2'),
            ]),
            junit.TestSuite([
                junit.TestCase(name='tc3', status='unknown'),
                junit.TestCase(),
            ], name='ts2'),
        ], name='xyz')
        xml = tr.toXml()
        xml = xml.decode('utf-8')
        self.assertEqual('<testsuites' in xml, True)
        self.assertEqual('name="xyz"' in xml, True)
        self.assertEqual('name="ts2"' in xml, True)
        self.assertEqual('name="tc1"' in xml, True)
        self.assertEqual('name="tc2"' in xml, True)
        self.assertEqual('name="tc3"' in xml, True)
        self.assertEqual('status="unknown"' in xml, True)
        self.assertEqual(len(re.findall('<testsuite ', xml)), 2)
        self.assertEqual(len(re.findall('<testcase', xml)), 4)

    def testComplexEncoding3(self):
        tr = junit.TestReport([
            junit.TestSuite([
                junit.TestCase(name='tc1', classname='tc1c'),
                junit.TestCase(name='tc2', status='unknown', time=5),
            ]),
            junit.TestSuite([
                junit.TestCase(name='tc3', time=1),
                junit.TestCase(time='5.5'),
            ], name='ts2'),
        ], name='xyz')
        xml = tr.toXml()
        xml = xml.decode('utf-8')
        self.assertEqual('<testsuites' in xml, True)
        self.assertEqual('name="xyz"' in xml, True)
        self.assertEqual('name="ts2"' in xml, True)
        self.assertEqual('name="tc1"' in xml, True)
        self.assertEqual('name="tc2"' in xml, True)
        self.assertEqual('name="tc3"' in xml, True)
        self.assertEqual('time="5' in xml, True)
        self.assertEqual('time="1' in xml, True)
        self.assertEqual('time="5.5' in xml, True)
        self.assertEqual('time="6.5' in xml, True)
        self.assertEqual('time="11.5' in xml, True)
        self.assertEqual(len(re.findall('<testsuite ', xml)), 2)
        self.assertEqual(len(re.findall('<testcase ', xml)), 4)

    def testComplexEncoding4(self):
        tr = junit.TestReport([
            junit.TestSuite([
                junit.TestCase(skipped=''),
                junit.TestCase(failure=''),
                junit.TestCase(error=''),
                junit.TestCase(systemOut='', systemErr=''),
            ]),
            junit.TestSuite([
                junit.TestCase(skipped=''),
                junit.TestCase(failure=''),
                junit.TestCase(failure=''),
                junit.TestCase(error=''),
                junit.TestCase(error=''),
                junit.TestCase(error=''),
            ]),
        ])
        xml = tr.toXml()
        xml = xml.decode('utf-8')
        self.assertEqual(len(re.findall('<testsuites ', xml)), 1)
        self.assertEqual(len(re.findall('<testsuite ', xml)), 2)
        self.assertEqual(len(re.findall('<testcase', xml)), 10)
        self.assertEqual(len(re.findall('<skipped', xml)), 2)
        self.assertEqual(len(re.findall('<failure', xml)), 3)
        self.assertEqual(len(re.findall('<error', xml)), 4)
        self.assertEqual(len(re.findall('<system-out', xml)), 1)
        self.assertEqual(len(re.findall('<system-err', xml)), 1)

    def testComplexEncoding5(self):
        tr = junit.TestReport([
            junit.TestSuite([
                junit.TestCase(skipped='yes'),
                junit.TestCase(failure='some_fail'),
                junit.TestCase(error='some_err'),
                junit.TestCase(systemOut='some_sout', systemErr='some_serr'),
            ]),
            junit.TestSuite([
                junit.TestCase(skipped='yes'),
                junit.TestCase(failure='some_fail'),
                junit.TestCase(failure='some_fail'),
                junit.TestCase(error='some_err'),
                junit.TestCase(error='some_err'),
                junit.TestCase(error='some_err'),
            ]),
        ])
        xml = tr.toXml()
        xml = xml.decode('utf-8')
        self.assertEqual(len(re.findall('yes', xml)), 2)
        self.assertEqual(len(re.findall('some_fail', xml)), 3)
        self.assertEqual(len(re.findall('some_err', xml)), 4)
        self.assertEqual(len(re.findall('some_sout', xml)), 1)
        self.assertEqual(len(re.findall('some_serr', xml)), 1)
        self.assertEqual(len(re.findall('<testsuites ', xml)), 1)
        self.assertEqual(len(re.findall('<testsuite ', xml)), 2)
        self.assertEqual(len(re.findall('<testcase', xml)), 10)
        self.assertEqual(len(re.findall('<skipped', xml)), 2)
        self.assertEqual(len(re.findall('<failure', xml)), 3)
        self.assertEqual(len(re.findall('<error', xml)), 4)
        self.assertEqual(len(re.findall('<system-out', xml)), 1)
        self.assertEqual(len(re.findall('<system-err', xml)), 1)

    def testComplexEncoding6(self):
        tr = junit.TestReport([
            junit.TestSuite([
                junit.TestCase(failure='some_fail', failure_message='msg', failure_type='type'),
            ]),
        ])
        xml = tr.toXml()
        xml = xml.decode('utf-8')
        self.assertEqual(len(re.findall('some_fail', xml)), 1)
        self.assertEqual(len(re.findall('message="msg"', xml)), 1)
        self.assertEqual(len(re.findall('type="type"', xml)), 1)
        self.assertEqual(len(re.findall('<testsuites ', xml)), 1)
        self.assertEqual(len(re.findall('<testsuite ', xml)), 1)
        self.assertEqual(len(re.findall('<testcase', xml)), 1)
        self.assertEqual(len(re.findall('<failure', xml)), 1)

    def testComplexEncoding7(self):
        tr = junit.TestReport([
            junit.TestSuite([
                junit.TestCase(failure_message='msg', failure_type='type'),
            ]),
        ])
        xml = tr.toXml()
        xml = xml.decode('utf-8')
        self.assertEqual(len(re.findall('message="msg"', xml)), 1)
        self.assertEqual(len(re.findall('type="type"', xml)), 1)
        self.assertEqual(len(re.findall('<testsuites ', xml)), 1)
        self.assertEqual(len(re.findall('<testsuite ', xml)), 1)
        self.assertEqual(len(re.findall('<testcase', xml)), 1)
        self.assertEqual(len(re.findall('<failure', xml)), 1)

    def testComplexEncoding8(self):
        tr = junit.TestReport([
            junit.TestSuite([
                junit.TestCase(error='some_err', error_message='msg', error_type='type'),
            ]),
        ])
        xml = tr.toXml()
        xml = xml.decode('utf-8')
        self.assertEqual(len(re.findall('some_err', xml)), 1)
        self.assertEqual(len(re.findall('message="msg"', xml)), 1)
        self.assertEqual(len(re.findall('type="type"', xml)), 1)
        self.assertEqual(len(re.findall('<testsuites ', xml)), 1)
        self.assertEqual(len(re.findall('<testsuite ', xml)), 1)
        self.assertEqual(len(re.findall('<testcase', xml)), 1)
        self.assertEqual(len(re.findall('<error', xml)), 1)

    def testComplexEncoding9(self):
        tr = junit.TestReport([
            junit.TestSuite([
                junit.TestCase(error_message='msg', error_type='type'),
            ]),
        ])
        xml = tr.toXml()
        xml = xml.decode('utf-8')
        self.assertEqual(len(re.findall('message="msg"', xml)), 1)
        self.assertEqual(len(re.findall('type="type"', xml)), 1)
        self.assertEqual(len(re.findall('<testsuites ', xml)), 1)
        self.assertEqual(len(re.findall('<testsuite ', xml)), 1)
        self.assertEqual(len(re.findall('<testcase', xml)), 1)
        self.assertEqual(len(re.findall('<error', xml)), 1)

    def testComplexEncoding9(self):
        tr = junit.TestReport([
            junit.TestSuite([
                junit.TestCase(error_message='msg', error_type='type'),
            ]),
        ])
        uglyXml = tr.toXml()
        prettyXml = tr.toXml(prettyPrint=True)
        self.assertEqual(len(uglyXml) < len(prettyXml), True)


    # TODO: encode-decode-check
    # TODO: merge
    # TODO: decode-merge-check


if __name__ == '__main__':
    unittest.main()
