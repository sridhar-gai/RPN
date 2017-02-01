from operators.addition_operator import AdditionOperator
from operators.subtraction_operator import SubtractionOperator
from operators.multiplication_operator import MultiplicationOperator
from operators.division_operator import DivisionOperator
from operators.exponentiation_operator import ExponentiationOperator
from operators.factorial_operator import FactorialOperator
from operators.percentage_operator import PercentageOperator


class OperatorFactory(object):
    def __init__(self):
        self.operator_class_map = {"+": AdditionOperator, "-": SubtractionOperator, "*": MultiplicationOperator,
                                   "/": DivisionOperator, "^": ExponentiationOperator, "%": PercentageOperator,
                                   "!": FactorialOperator}

    def get_operator_instance(self, operator):
        return self.operator_class_map[operator]()
