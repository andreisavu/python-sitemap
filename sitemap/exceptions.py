
class InvalidUrl(ValueError):
    def __init__(self, msg='Invalid URL'):
        ValueError.__init__(self, msg)

class InvalidDate(ValueError):
    def __init__(self, msg='Invalid datetime'):
        ValueError.__init__(self, msg)

class InvalidChangeFreq(ValueError):
    def __init__(self, msg='Invalid change frequency'):
        ValueError.__init__(self, msg)


