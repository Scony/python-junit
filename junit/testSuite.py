class TestSuite(object):


    def __init__(self, testCases=None, **kwargs):
        self.params = {
            'time': None,
            'name': None,
            'tests': None,
            'skipped': None,
            'failures': None,
            'errors': None,
            'testCases': [],
            'timeAggregate': sum,
        }

        if 'timeAggregate' in kwargs and kwargs['timeAggregate'] is not None:
            self.params['timeAggregate'] = kwargs['timeAggregate']

        if testCases is not None and not isinstance(testCases, list):
            testCases = [testCases]

        if testCases is not None:
            def anything2float(anything):
                try:
                    return float(anything)
                except:
                    return None

            testCasesTimes = [anything2float(tc.params['time']) for tc in testCases]
            testCasesTimes = [time for time in testCasesTimes if time is not None]
            if len(testCasesTimes) > 0:
                self.params['time'] = self.params['timeAggregate'](testCasesTimes)

            self.params['tests'] = len(testCases)
            self.params['skipped'] = len([tc for tc in testCases if
                                          tc.params['skipped'] is not None and
                                          tc.params['failure'] is None and
                                          tc.params['error'] is None])
            self.params['failures'] = len([tc for tc in testCases if
                                          tc.params['skipped'] is None and
                                          tc.params['failure'] is not None and
                                          tc.params['error'] is None])
            self.params['errors'] = len([tc for tc in testCases if
                                          tc.params['skipped'] is None and
                                          tc.params['failure'] is None and
                                          tc.params['error'] is not None])
            self.params['testCases'] = testCases

        self.params.update(kwargs)


    def __str__(self):
        return str(self.params)
