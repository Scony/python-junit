test:
	@python -m tests.basicTests
	@python -m tests.testCaseTests

all: test
