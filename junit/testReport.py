class TestReport(object):

    def __init__(self, testSuites=None, **kwargs):
        self.params = {
            'time': None,
            'name': None,
            'tests': None,
            'failures': None,
            'disabled': None,
            'testSuites': [],
            'timeAggreate': sum,
        }

        if testSuites is not None:
            pass                # TODO: fill with testSuites

        self.params.update(kwargs)

    def toXml(self):
        pass

    def fromXml(self, xmlStr):
        pass

    def merge(self, testReport):
        pass

    def __str__(self):
        return str(self.params)
