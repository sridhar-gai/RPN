from abc import ABCMeta


class Operator(object):
    def __init__(self):
        self._num_operands = None

    __metaclass__ = ABCMeta

    def operate(self, *args):
        pass

    def get_num_operands(self):
        return self._num_operands
