test:
	@python -m tests.basicTests
	@python -m tests.testCaseTests
	@python -m tests.testSuiteTests
	@python -m tests.testReportTests

all: test
