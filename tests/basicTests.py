import unittest
import junit


class TestBasicStuff(unittest.TestCase):

    def testClassesPresent(self):
        self.assertEqual(isinstance(junit.TestCase, object), True)
        self.assertEqual(isinstance(junit.TestSuite, object), True)
        self.assertEqual(isinstance(junit.TestReport, object), True)

    def testEmptyConstructors(self):
        self.assertEqual(isinstance(junit.TestCase(), object), True)
        self.assertEqual(isinstance(junit.TestSuite(), object), True)
        self.assertEqual(isinstance(junit.TestReport(), object), True)

    def testKWArgConstructors(self):
        self.assertEqual(isinstance(junit.TestCase(a=1,b=1,c=1), object), True)
        self.assertEqual(isinstance(junit.TestSuite(a=1,b=1,c=1), object), True)
        self.assertEqual(isinstance(junit.TestReport(a=1,b=1,c=1), object), True)


if __name__ == '__main__':
    unittest.main()
