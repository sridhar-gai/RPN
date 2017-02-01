from operator import Operator


class PercentageOperator(Operator):
    def __init__(self):
        self._num_operands = 1

    def operate(self, *args):
        return float(args[0]) / 100
