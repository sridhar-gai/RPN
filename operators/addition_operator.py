from operator import Operator


class AdditionOperator(Operator):
    def __init__(self):
        self._num_operands = 2

    def operate(self, *args):
        return args[0] + args[1]
