import unittest
import junit


class TestTestSuite(unittest.TestCase):

    def testParametersSetting1(self):
        ts = junit.TestSuite(
            failures='5',
            name='bbb',
        )
        self.assertEqual(ts.params['time'], None)
        self.assertEqual(ts.params['name'], 'bbb')
        self.assertEqual(ts.params['tests'], None)
        self.assertEqual(ts.params['skipped'], None)
        self.assertEqual(ts.params['failures'], '5')
        self.assertEqual(ts.params['errors'], None)
        self.assertEqual(ts.params['testCases'], [])
        self.assertEqual(ts.params['timeAggregate'], sum)

    def testParametersSetting2(self):
        ts = junit.TestSuite(
            name='bbb',
            failures=5,
        )
        self.assertEqual(ts.params['time'], None)
        self.assertEqual(ts.params['name'], 'bbb')
        self.assertEqual(ts.params['tests'], None)
        self.assertEqual(ts.params['skipped'], None)
        self.assertEqual(ts.params['failures'], 5)
        self.assertEqual(ts.params['errors'], None)
        self.assertEqual(ts.params['testCases'], [])
        self.assertEqual(ts.params['timeAggregate'], sum)

    def testParametersSetting3(self):
        ts = junit.TestSuite(
            time=7,
            name='bbb',
            tests='55',
            skipped='xxx',
            failures=5,
            errors=11,
        )
        self.assertEqual(ts.params['time'], 7)
        self.assertEqual(ts.params['name'], 'bbb')
        self.assertEqual(ts.params['tests'], '55')
        self.assertEqual(ts.params['skipped'], 'xxx')
        self.assertEqual(ts.params['failures'], 5)
        self.assertEqual(ts.params['errors'], 11)
        self.assertEqual(ts.params['testCases'], [])
        self.assertEqual(ts.params['timeAggregate'], sum)

    def testParametersSetting4(self):
        ts = junit.TestSuite(
            timeAggregate=min,
        )
        self.assertEqual(ts.params['timeAggregate'], min)

    def testParametersSetting5(self):
        tcs = [junit.TestCase() for _ in range(3)]
        ts = junit.TestSuite(
            tcs,
            name='xxx',
        )
        self.assertEqual(ts.params['name'], 'xxx')
        self.assertEqual(len(ts.params['testCases']), 3)

    def testParametersSetting6(self):
        tcs = [junit.TestCase() for _ in range(3)]
        ts = junit.TestSuite(
            name='xxx',
            testCases=tcs,
        )
        self.assertEqual(ts.params['name'], 'xxx')
        self.assertEqual(len(ts.params['testCases']), 3)

    def testParametersSetting7(self):
        tcs = junit.TestCase()
        ts = junit.TestSuite(
            name='xxx',
            testCases=tcs,
        )
        self.assertEqual(ts.params['name'], 'xxx')
        self.assertEqual(len(ts.params['testCases']), 1)

    def testParametersCalculation1(self):
        tcs = [junit.TestCase() for _ in range(3)]
        ts = junit.TestSuite(
            name='xxx',
            testCases=tcs,
        )
        self.assertEqual(ts.params['tests'], 3)
        self.assertEqual(len(ts.params['testCases']), 3)

    def testParametersCalculation2(self):
        tcs = [
            junit.TestCase(name='xxx'),
            junit.TestCase(skipped=True),
            junit.TestCase(failure=True),
            junit.TestCase(failure=True),
            junit.TestCase(error=True),
            junit.TestCase(error=True),
            junit.TestCase(error=True),
        ]
        ts = junit.TestSuite(tcs)
        self.assertEqual(ts.params['time'], None)
        self.assertEqual(ts.params['tests'], 7)
        self.assertEqual(ts.params['skipped'], 1)
        self.assertEqual(ts.params['failures'], 2)
        self.assertEqual(ts.params['errors'], 3)
        self.assertEqual(len(ts.params['testCases']), 7)

    def testParametersCalculation3(self):
        tcs = [
            junit.TestCase(time=1, name='xxx'),
            junit.TestCase(time=2, skipped=True),
            junit.TestCase(failure=True),
            junit.TestCase(time='3.3', failure=True),
            junit.TestCase(error=True),
            junit.TestCase(time=3.3, error=True),
            junit.TestCase(error=True),
        ]
        ts = junit.TestSuite(tcs)
        self.assertEqual(ts.params['time'], sum([float(1), float(2), float('3.3'), float(3.3)]))
        self.assertEqual(ts.params['tests'], 7)
        self.assertEqual(ts.params['skipped'], 1)
        self.assertEqual(ts.params['failures'], 2)
        self.assertEqual(ts.params['errors'], 3)
        self.assertEqual(len(ts.params['testCases']), 7)

    def testParametersCalculation4(self):
        tcs = [
            junit.TestCase(time=1, name='xxx'),
            junit.TestCase(time=2, skipped=True),
            junit.TestCase(failure=True),
            junit.TestCase(time='3.7', failure=True),
            junit.TestCase(error=True),
            junit.TestCase(time=3.3, error=True),
            junit.TestCase(error=True),
        ]
        ts = junit.TestSuite(tcs, timeAggregate=max)
        self.assertEqual(ts.params['time'], max([float(1), float(2), float('3.7'), float(3.3)]))
        self.assertEqual(ts.params['tests'], 7)
        self.assertEqual(ts.params['skipped'], 1)
        self.assertEqual(ts.params['failures'], 2)
        self.assertEqual(ts.params['errors'], 3)
        self.assertEqual(len(ts.params['testCases']), 7)

    def testParametersOverride(self):
        tcs = [
            junit.TestCase(time=1, name='xxx'),
            junit.TestCase(time=2, skipped=True),
            junit.TestCase(failure=True),
            junit.TestCase(time='3.7', failure=True),
            junit.TestCase(error=True),
            junit.TestCase(time=3.3, error=True),
            junit.TestCase(error=True),
        ]
        ts = junit.TestSuite(tcs, timeAggregate=max, skipped=777)
        self.assertEqual(ts.params['time'], max([float(1), float(2), float('3.7'), float(3.3)]))
        self.assertEqual(ts.params['tests'], 7)
        self.assertEqual(ts.params['skipped'], 777)
        self.assertEqual(ts.params['failures'], 2)
        self.assertEqual(ts.params['errors'], 3)
        self.assertEqual(len(ts.params['testCases']), 7)


if __name__ == '__main__':
    unittest.main()
