import unittest
import junit


class TestTestReport(unittest.TestCase):

    def testParametersSetting1(self):
        tr = junit.TestReport(
            name='bbb',
            failures='5',
        )
        self.assertEqual(tr.params['time'], None)
        self.assertEqual(tr.params['name'], 'bbb')
        self.assertEqual(tr.params['tests'], None)
        self.assertEqual(tr.params['failures'], '5')
        self.assertEqual(tr.params['testSuites'], [])
        self.assertEqual(tr.params['timeAggregate'], sum)

    def testParametersSetting2(self):
        tr = junit.TestReport(
            name='bbb',
            failures=7,
        )
        self.assertEqual(tr.params['time'], None)
        self.assertEqual(tr.params['name'], 'bbb')
        self.assertEqual(tr.params['tests'], None)
        self.assertEqual(tr.params['failures'], 7)
        self.assertEqual(tr.params['testSuites'], [])
        self.assertEqual(tr.params['timeAggregate'], sum)

    def testParametersSetting3(self):
        tr = junit.TestReport(
            time=10,
            name='bbb',
            tests='ccc',
            failures=7,
            timeAggregate=min,
        )
        self.assertEqual(tr.params['time'], 10)
        self.assertEqual(tr.params['name'], 'bbb')
        self.assertEqual(tr.params['tests'], 'ccc')
        self.assertEqual(tr.params['failures'], 7)
        self.assertEqual(tr.params['testSuites'], [])
        self.assertEqual(tr.params['timeAggregate'], min)

    def testParametersSetting4(self):
        tss = [junit.TestSuite() for _ in range(3)]
        tr = junit.TestReport(
            tss,
            name='yyy',
        )
        self.assertEqual(tr.params['name'], 'yyy')
        self.assertEqual(len(tr.params['testSuites']), 3)

    def testParametersSetting5(self):
        tss = [junit.TestSuite() for _ in range(3)]
        tr = junit.TestReport(
            name='yyy',
            testSuites=tss,
        )
        self.assertEqual(tr.params['name'], 'yyy')
        self.assertEqual(len(tr.params['testSuites']), 3)

    def testParametersSetting6(self):
        tss = junit.TestSuite()
        tr = junit.TestReport(
            name='yyy',
            testSuites=tss,
        )
        self.assertEqual(tr.params['name'], 'yyy')
        self.assertEqual(len(tr.params['testSuites']), 1)

    def testParametersCalculation1(self):
        tss = junit.TestSuite(tests=1)
        tr = junit.TestReport(tss)
        self.assertEqual(len(tr.params['testSuites']), 1)
        self.assertEqual(tr.params['tests'], 1)

    def testParametersCalculation2(self):
        tss = [
            junit.TestSuite(tests=1),
            junit.TestSuite(tests='2'),
            junit.TestSuite(tests=3),
        ]
        tr = junit.TestReport(tss)
        self.assertEqual(tr.params['tests'], 6)
        self.assertEqual(len(tr.params['testSuites']), 3)

    def testParametersCalculation3(self):
        tss = [
            junit.TestSuite(failures='3', tests=1),
            junit.TestSuite(failures=2, tests='2'),
            junit.TestSuite(failures='xxx', tests=3),
        ]
        tr = junit.TestReport(tss)
        self.assertEqual(tr.params['tests'], 6)
        self.assertEqual(tr.params['failures'], 5)
        self.assertEqual(len(tr.params['testSuites']), 3)

    def testParametersCalculation4(self):
        tss = [
            junit.TestSuite(time=1),
            junit.TestSuite(time=2),
            junit.TestSuite(time='3.3'),
            junit.TestSuite(time=3.7),
        ]
        tr = junit.TestReport(tss)
        self.assertEqual(tr.params['time'], sum([float(1), float(2), float('3.3'), float(3.7)]))
        self.assertEqual(len(tr.params['testSuites']), 4)

    def testParametersCalculation5(self):
        tss = [
            junit.TestSuite(time=1),
            junit.TestSuite(time=2),
            junit.TestSuite(time='3.3'),
            junit.TestSuite(time=3.7),
        ]
        tr = junit.TestReport(tss, timeAggregate=min)
        self.assertEqual(tr.params['time'], min([float(1), float(2), float('3.3'), float(3.7)]))
        self.assertEqual(len(tr.params['testSuites']), 4)

    def testParametersCalculation6(self):
        tss = [
            junit.TestSuite(errors='3', tests=1),
            junit.TestSuite(errors=2, tests='2'),
            junit.TestSuite(errors='xxx', tests=3),
        ]
        tr = junit.TestReport(tss)
        self.assertEqual(tr.params['tests'], 6)
        self.assertEqual(tr.params['errors'], 5)
        self.assertEqual(len(tr.params['testSuites']), 3)

    def testParametersOverride(self):
        tss = [
            junit.TestSuite(time=1),
            junit.TestSuite(time=2),
            junit.TestSuite(time='3.3'),
            junit.TestSuite(time=3.7),
        ]
        tr = junit.TestReport(tss, timeAggregate=min, time=777)
        self.assertEqual(tr.params['time'], 777)
        self.assertEqual(len(tr.params['testSuites']), 4)


if __name__ == '__main__':
    unittest.main()
