def is_valid_operand(operand):
    try:
        int(operand)
        return True
    except ValueError:
        try:
            float(operand)
            return True
        except ValueError:
            return False


def extract_number(number):
    try:
        return int(number)
    except ValueError:
        try:
            return float(number)
        except ValueError:
            raise


def pop_operands(operand_instance, operand_stack):
    num_operands = operand_instance.get_num_operands()
    operands_list = []
    for i in xrange(num_operands):
        operands_list.insert(0, operand_stack.pop())
    return operands_list
