class TestCase(object):


    def __init__(self, **kwargs):
        self.params = {
            'time': None,
            'classname': None,
            'name': None,
            'status': None,
            'skipped': None,
            'failure': None,
            'error': None,
            'systemOut': None,
            'systemErr': None,
        }
        self.params.update(kwargs)


    def __str__(self):
        return str(self.params)
