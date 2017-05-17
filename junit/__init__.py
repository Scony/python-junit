"""
Based on:
* Personal expiriences with JUnit Jenkins Plugin
* http://stackoverflow.com/questions/4922867/junit-xml-format-specification-that-hudson-supports
* https://github.com/kyrus/python-junit-xml
"""

from . import testCase
from . import testSuite
from . import testReport

class TestCase(testCase.TestCase):
    pass

class TestSuite(testSuite.TestSuite):
    pass

class TestReport(testReport.TestReport):
    pass
