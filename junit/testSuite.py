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
            'timeAggreate': sum,
        }

        if testCases is not None:
            pass                # TODO: fill with testCases

        self.params.update(kwargs)

    def __str__(self):
        return str(self.params)
