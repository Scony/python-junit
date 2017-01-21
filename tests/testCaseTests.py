import unittest
import junit


class TestTestCase(unittest.TestCase):

    def testParametersSetting1(self):
        tc = junit.TestCase(
            classname='aaa',
            name='bbb',
        )
        self.assertEqual(tc.params['time'], None)
        self.assertEqual(tc.params['classname'], 'aaa')
        self.assertEqual(tc.params['name'], 'bbb')
        self.assertEqual(tc.params['status'], None)
        self.assertEqual(tc.params['skipped'], None)
        self.assertEqual(tc.params['failure'], None)
        self.assertEqual(tc.params['error'], None)
        self.assertEqual(tc.params['systemOut'], None)
        self.assertEqual(tc.params['systemErr'], None)

    def testParametersSetting2(self):
        tc = junit.TestCase(
            time=0.1,
            classname='aaa',
            name='bbb',
            status='ccc',
            skipped='ddd',
            failure='eee',
            error='fff',
            systemOut='ggg',
            systemErr='hhh',
        )
        self.assertEqual(tc.params['time'], 0.1)
        self.assertEqual(tc.params['classname'], 'aaa')
        self.assertEqual(tc.params['name'], 'bbb')
        self.assertEqual(tc.params['status'], 'ccc')
        self.assertEqual(tc.params['skipped'], 'ddd')
        self.assertEqual(tc.params['failure'], 'eee')
        self.assertEqual(tc.params['error'], 'fff')
        self.assertEqual(tc.params['systemOut'], 'ggg')
        self.assertEqual(tc.params['systemErr'], 'hhh')

    def testParametersSetting3(self):
        tc = junit.TestCase(
            time='0.1',
            classname='aaa',
            name='bbb',
            status='ccc',
            skipped='ddd',
            failure='eee',
            error='fff',
            systemOut='ggg',
            systemErr='hhh',
        )
        self.assertEqual(tc.params['time'], '0.1')
        self.assertEqual(tc.params['classname'], 'aaa')
        self.assertEqual(tc.params['name'], 'bbb')
        self.assertEqual(tc.params['status'], 'ccc')
        self.assertEqual(tc.params['skipped'], 'ddd')
        self.assertEqual(tc.params['failure'], 'eee')
        self.assertEqual(tc.params['error'], 'fff')
        self.assertEqual(tc.params['systemOut'], 'ggg')
        self.assertEqual(tc.params['systemErr'], 'hhh')


if __name__ == '__main__':
    unittest.main()
