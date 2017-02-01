from business.main import NOT_A_VALID_OPERATOR, UNSUPPORTED_OPERATION_ERROR, INVALID_EXPRESSION_ERROR, \
    DIVIDE_BY_ZERO_ERROR, DELIMITER

ERROR_MAP = {NOT_A_VALID_OPERATOR: 'Given expression contains an invalid operator',
             UNSUPPORTED_OPERATION_ERROR: 'In compatible data type found when executing the given expression',
             INVALID_EXPRESSION_ERROR: 'The given expression is an invalid RPN expression',
             DIVIDE_BY_ZERO_ERROR: 'Got divide by zero error when evaluating the given expression'}

HELP_TEXT = "In Reverse Polish Notation (RPN), the operators follow their operands. Eg., RPN form of the expression " \
            "'3+4' is '3{}4{}+'".format(DELIMITER, DELIMITER)
