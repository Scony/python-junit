python-junit
============

![Build status](https://travis-ci.org/Scony/python-junit.svg?branch=master)

About
-----

This module is a semi-automatic tool for generating JUnit XML reports consumed by JUnit Jenkins Plugin.

It is semi-automatic since the user must provide some necessary information about particular report parts.

Basic example
-------------

In order to create a report and generate XML, you need to create a `TestReport` object and call `toXml()` method on it.

`TestReport` can contain some `TestSuite` objects which can contain some `TestCase` objects.

In order to set parameters, `kwargs` need to be passed to the object while constructing. If you want to avoid auto-calcualtion of particular field, you can set it to `None`.

~~~python
from junit import TestCase, TestSuite, TestReport

tc1 = TestCase(name='test1', time=5.5)
tc2 = TestCase(name='test2', failure='some failure details', failure_message='exception caught during startup')
tc3 = TestCase(name='test3', skipped='')
tc4 = TestCase(error='some very bad error', time='7.7')
tc5 = TestCase(skipped='yes')
tc6 = TestCase()

ts1 = TestSuite([tc1, tc2, tc3, tc4], name='suite1')
ts2 = TestSuite([tc5], name='suite2')
ts3 = TestSuite(tc6, name='suite3', errors=None, failures=None, skipped=None, tests=None)

report = TestReport([ts1, ts2, ts3], name='MyReport')

print report.toXml(prettyPrint=True)
~~~

~~~
<?xml version="1.0" ?>
<testsuites failures="1" name="MyReport" tests="5" time="13.2">
	<testsuite errors="1" failures="1" name="suite1" skipped="1" tests="4" time="13.2">
		<testcase name="test1" time="5.5"/>
		<testcase name="test2">
			<failure message="exception caught during startup">some failure details</failure>
		</testcase>
		<testcase name="test3">
			<skipped/>
		</testcase>
		<testcase time="7.7">
			<error>some very bad error</error>
		</testcase>
	</testsuite>
	<testsuite errors="0" failures="0" name="suite2" skipped="1" tests="1">
		<testcase>
			<skipped>yes</skipped>
		</testcase>
	</testsuite>
	<testsuite name="suite3">
		<testcase/>
	</testsuite>
</testsuites>

~~~

Testing
-------

In order to run the tests you need to call a `test` target from `makefile`:

~~~bash
$ make test
~~~

TODO:
-----

* decoding from XML to `TestReport` object + child objects
* merging multiple `TestReport` to one
* illegal characters filtering
* refactoring
