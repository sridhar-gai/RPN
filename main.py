from custom_exceptions.unsupported_operation import UnSupportedOperationForDataType
from factory import OperatorFactory
from rpn_utils import is_valid_operand, extract_number, pop_operands

ERROR = "ERROR"
NOT_A_VALID_OPERAND = "ERROR"
DIVIDE_BY_ZERO_ERROR = "ERROR"
INVALID_EXPRESSION_ERROR = "ERROR"
UNSUPPORTED_OPERATION_ERROR = "ERROR"
DELIMITER = ","


class RPNCalculator(object):
    def __init__(self, expression):
        self.expression = expression
        self.operator_factory = OperatorFactory()

    def perform_operation(self, operand_stack, operator):
        operand_instance = self.operator_factory.get_operator_instance(operator)
        operands_list = pop_operands(operand_instance, operand_stack)
        return operand_instance.operate(*operands_list)

    def is_valid_operator(self, token):
        return token in self.operator_factory.operator_class_map

    def evaluate_rpn(self):
        operand_stack = list([])

        try:
            input_list = self.expression.split(DELIMITER)
            for item in input_list:
                if self.is_valid_operator(item):
                    partial_result = self.perform_operation(operand_stack, item)
                    operand_stack.append(partial_result)
                elif is_valid_operand(item):
                    operand_stack.append(extract_number(item))
                else:
                    return NOT_A_VALID_OPERAND
            result = operand_stack.pop()
            if not operand_stack:
                return result
            else:
                return ERROR
        except IndexError:
            return INVALID_EXPRESSION_ERROR
        except UnSupportedOperationForDataType:
            return UNSUPPORTED_OPERATION_ERROR
        except ZeroDivisionError:
            return DIVIDE_BY_ZERO_ERROR
