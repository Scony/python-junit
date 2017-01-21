class TestReport(object):


    def __init__(self, testSuites=None, **kwargs):
        self.params = {
            'time': None,
            'name': None,
            'tests': None,
            'failures': None,
            'disabled': None,
            'testSuites': [],
            'timeAggregate': sum,
        }

        if 'timeAggregate' in kwargs and kwargs['timeAggregate'] is not None:
            self.params['timeAggregate'] = kwargs['timeAggregate']

        if testSuites is not None and not isinstance(testSuites, list):
            testSuites = [testSuites]

        if testSuites is not None:
            def anything2int(anything):
                try:
                    return int(anything)
                except:
                    return None

            def anything2float(anything):
                try:
                    return float(anything)
                except:
                    return None

            timesInSuites = [anything2float(ts.params['time']) for ts in testSuites]
            timesInSuites = [time for time in timesInSuites if time is not None]
            self.params['time'] = self.params['timeAggregate'](timesInSuites)

            testsInSuites = [anything2int(ts.params['tests']) for ts in testSuites]
            testsInSuites = [tests for tests in testsInSuites if tests is not None]
            self.params['tests'] = sum(testsInSuites)

            failuresInSuites = [anything2int(ts.params['failures']) for ts in testSuites]
            failuresInSuites = [failures for failures in failuresInSuites if failures is not None]
            self.params['failures'] = sum(failuresInSuites)

            self.params['testSuites'] = testSuites

        self.params.update(kwargs)


    def toXml(self):
        pass


    def fromXml(self, xmlStr):
        pass


    def merge(self, testReport):
        pass


    def __str__(self):
        return str(self.params)
