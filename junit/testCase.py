class TestCase(object):
    def __init__(self, **kwargs):
        self.params = {
            'time': None,
        }
        self.params.update(kwargs)
