
class InvalidUrl(Exception):
    def __init__(self, msg='Invalid URL'):
        Exception.__init__(self, msg)



