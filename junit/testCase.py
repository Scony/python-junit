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
        self.attributeNames = [
            'time',
            'classname',
            'name',
            'status',
        ]
        self.childNames = {
            'skipped': 'skipped',
            'failure': 'failure',
            'error': 'error',
            'systemOut': 'system-out',
            'systemErr': 'system-err',
        }

        self.params.update(kwargs)


    def __str__(self):
        return str(self.params)


    def _fillAttributes(self, attributes): # TODO: remove and use **
        for attributeName in self.attributeNames:
            if attributeName in attributes:
                self.params[attributeName] = attributes[attributeName]
