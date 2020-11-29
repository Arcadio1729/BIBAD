class NonRealException(Exception):
    def __init__(self, message):
        super(NonRealException, self).__init__(message)

class NotQuadraticEquation(Exception):
    def __init__(self, message):
        super(NotQuadraticEquation, self).__init__(message)




class OnePointException(Exception):
    def __init__(self, message):
        super(OnePointException, self).__init__(message)