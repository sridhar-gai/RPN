from operator import Operator


class DivisionOperator(Operator):
    def __init__(self):
        self._num_operands = 2

    def operate(self, *args):
        result = float(args[0]) / args[1]
        if not result - int(result):
            result = int(result)
        return result
