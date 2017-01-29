from operator import Operator
from custom_exceptions.unsupported_operation import UnSupportedOperationForDataType


class FactorialOperator(Operator):
    def __init__(self):
        self._num_operands = 1

    def operate(self, *args):
        if not isinstance(args[0], int):
            raise UnSupportedOperationForDataType

        number = args[0]
        if number < 0:
            raise TypeError
        value = 1
        for x in xrange(number, 1, -1):
            value = value * x
        return value
