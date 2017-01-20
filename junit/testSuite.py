class TestSuite(object):
    def __init__(self, testCases=None, **kwargs):
        self.params = {
            'time': None,
            'testCases': None,
        }

        if testCases is not None:
            pass                # TODO: fill with testCases

        self.params.update(kwargs)
