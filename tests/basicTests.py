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

    def testTestCaseMethodsPresent(self):
        """TestCase must contain some assumed methods"""
        self.assertEqual(set([
            '__str__',          # exists anyway but we override it
        ]).issubset(dir(junit.TestCase)), True)

    def testTestSuiteMethodsPresent(self):
        """TestSuite must contain some assumed methods"""
        self.assertEqual(set([
            '__str__',          # exists anyway but we override it
        ]).issubset(dir(junit.TestSuite)), True)

    def testTestReportMethodsPresent(self):
        """TestReport must contain some assumed methods"""
        self.assertEqual(set([
            '__str__',          # exists anyway but we override it
            'toXml',
            'fromXml',
            'merge',
        ]).issubset(dir(junit.TestReport)), True)


if __name__ == '__main__':
    unittest.main()
