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
        self.attributeNames = [
            'time',
            'name',
            'tests',
            'skipped',
            'failures',
            'errors',
        ]

        if 'timeAggregate' in kwargs and kwargs['timeAggregate'] is not None:
            self.params['timeAggregate'] = kwargs['timeAggregate']

        if testCases is not None and not isinstance(testCases, list):
            testCases = [testCases]

        if testCases is not None:
            self.params['testCases'] = testCases
            self._recalculateParams()

        self.params.update(kwargs)


    def merge(self, testSuite, recalculate=True):
        testCaseNames = [tc.params['name'] for tc in self.params['testCases'] if tc.params['name'] is not None]
        testCasesToAdd = [tc for tc in testSuite.params['testCases'] if tc.params['name'] not in testCaseNames]
        testCasesToMerge = [tc for tc in testSuite.params['testCases'] if tc.params['name'] in testCaseNames]

        self.params['testCases'] += testCasesToAdd
        for i in range(len(self.params['testCases'])):
            for extTc in testCasesToMerge:
                if self.params['testCases'][i].params['name'] == extTc.params['name']:
                    self.params['testCases'][i] = extTc

        if recalculate:
            self._recalculateParams()


    def __str__(self):
        return str(self.params)


    def _fillAttributes(self, attributes): # TODO: remove and use **
        for attributeName in self.attributeNames:
            if attributeName in attributes:
                self.params[attributeName] = attributes[attributeName]


    def _recalculateParams(self):
        def anything2float(anything):
            try:
                return float(anything)
            except:
                return None

        testCasesTimes = [anything2float(tc.params['time']) for tc in self.params['testCases']]
        testCasesTimes = [time for time in testCasesTimes if time is not None]
        if len(testCasesTimes) > 0:
            self.params['time'] = self.params['timeAggregate'](testCasesTimes)

        self.params['tests'] = len(self.params['testCases'])
        self.params['skipped'] = len([tc for tc in self.params['testCases'] if
                                      tc.params['skipped'] is not None and
                                      tc.params['failure'] is None and
                                      tc.params['error'] is None])
        self.params['failures'] = len([tc for tc in self.params['testCases'] if
                                      tc.params['skipped'] is None and
                                      tc.params['failure'] is not None and
                                      tc.params['error'] is None])
        self.params['errors'] = len([tc for tc in self.params['testCases'] if
                                      tc.params['skipped'] is None and
                                      tc.params['failure'] is None and
                                      tc.params['error'] is not None])
