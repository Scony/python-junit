class TestReport(object):
    def __init__(self, testSuites=None, **kwargs):
        self.params = {
            'time': None,
            'testSuites': None,
        }

        if testSuites is not None:
            pass                # TODO: fill with testSuites

        self.params.update(kwargs)
