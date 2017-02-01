import pytest

from business.main import RPNCalculator, ERROR, DIVIDE_BY_ZERO_ERROR, INVALID_EXPRESSION_ERROR, \
    UNSUPPORTED_OPERATION_ERROR, NOT_A_VALID_OPERATOR, DELIMITER


class TestDataProvider(object):
    @staticmethod
    def get_parameterized_test_data():
        test_data = list([])
        # Basic checks
        test_data.append(("34".replace("|DELIM|", DELIMITER), 34))
        test_data.append(("4.33".replace("|DELIM|", DELIMITER), 4.33))
        test_data.append(("0|DELIM|!".replace("|DELIM|", DELIMITER), 1))
        test_data.append(("5|DELIM|2|DELIM|-".replace("|DELIM|", DELIMITER), 3))
        test_data.append(("5|DELIM|3|DELIM|-".replace("|DELIM|", DELIMITER), 2))
        test_data.append(("5|DELIM|3|DELIM|*".replace("|DELIM|", DELIMITER), 15))
        test_data.append(("15|DELIM|3|DELIM|/".replace("|DELIM|", DELIMITER), 5))

        # Commutation/Associativity checks
        test_data.append(("1|DELIM|2|DELIM|3|DELIM|+|DELIM|+".replace("|DELIM|", DELIMITER), 6))
        test_data.append(("1|DELIM|3|DELIM|2|DELIM|+|DELIM|+".replace("|DELIM|", DELIMITER), 6))
        test_data.append(("2|DELIM|1|DELIM|3|DELIM|+|DELIM|+".replace("|DELIM|", DELIMITER), 6))
        test_data.append(("2|DELIM|3|DELIM|1|DELIM|+|DELIM|+".replace("|DELIM|", DELIMITER), 6))
        test_data.append(("3|DELIM|2|DELIM|1|DELIM|+|DELIM|+".replace("|DELIM|", DELIMITER), 6))
        test_data.append(("3|DELIM|1|DELIM|2|DELIM|+|DELIM|+".replace("|DELIM|", DELIMITER), 6))

        test_data.append(("1|DELIM|2|DELIM|3|DELIM|-|DELIM|-".replace("|DELIM|", DELIMITER), 2))
        test_data.append(("1|DELIM|3|DELIM|2|DELIM|-|DELIM|-".replace("|DELIM|", DELIMITER), 0))
        test_data.append(("2|DELIM|1|DELIM|3|DELIM|-|DELIM|-".replace("|DELIM|", DELIMITER), 4))
        test_data.append(("2|DELIM|3|DELIM|1|DELIM|-|DELIM|-".replace("|DELIM|", DELIMITER), 0))
        test_data.append(("3|DELIM|2|DELIM|1|DELIM|-|DELIM|-".replace("|DELIM|", DELIMITER), 2))
        test_data.append(("3|DELIM|1|DELIM|2|DELIM|-|DELIM|-".replace("|DELIM|", DELIMITER), 4))

        test_data.append(("1|DELIM|2|DELIM|3|DELIM|*|DELIM|*".replace("|DELIM|", DELIMITER), 6))
        test_data.append(("1|DELIM|3|DELIM|2|DELIM|*|DELIM|*".replace("|DELIM|", DELIMITER), 6))
        test_data.append(("2|DELIM|1|DELIM|3|DELIM|*|DELIM|*".replace("|DELIM|", DELIMITER), 6))
        test_data.append(("2|DELIM|3|DELIM|1|DELIM|*|DELIM|*".replace("|DELIM|", DELIMITER), 6))
        test_data.append(("3|DELIM|2|DELIM|1|DELIM|*|DELIM|*".replace("|DELIM|", DELIMITER), 6))
        test_data.append(("3|DELIM|1|DELIM|2|DELIM|*|DELIM|*".replace("|DELIM|", DELIMITER), 6))

        test_data.append(("1|DELIM|2|DELIM|4|DELIM|/|DELIM|/".replace("|DELIM|", DELIMITER), 2))
        test_data.append(("1|DELIM|4|DELIM|2|DELIM|/|DELIM|/".replace("|DELIM|", DELIMITER), 0.5))
        test_data.append(("2|DELIM|1|DELIM|4|DELIM|/|DELIM|/".replace("|DELIM|", DELIMITER), 8))
        test_data.append(("2|DELIM|4|DELIM|1|DELIM|/|DELIM|/".replace("|DELIM|", DELIMITER), 0.5))
        test_data.append(("4|DELIM|2|DELIM|1|DELIM|/|DELIM|/".replace("|DELIM|", DELIMITER), 2))
        test_data.append(("4|DELIM|1|DELIM|2|DELIM|/|DELIM|/".replace("|DELIM|", DELIMITER), 8))

        test_data.append(("1|DELIM|2|DELIM|3|DELIM|^|DELIM|^".replace("|DELIM|", DELIMITER), 1))
        test_data.append(("1|DELIM|3|DELIM|2|DELIM|^|DELIM|^".replace("|DELIM|", DELIMITER), 1))
        test_data.append(("2|DELIM|1|DELIM|3|DELIM|^|DELIM|^".replace("|DELIM|", DELIMITER), 2))
        test_data.append(("2|DELIM|3|DELIM|1|DELIM|^|DELIM|^".replace("|DELIM|", DELIMITER), 8))
        test_data.append(("3|DELIM|2|DELIM|1|DELIM|^|DELIM|^".replace("|DELIM|", DELIMITER), 9))
        test_data.append(("3|DELIM|1|DELIM|2|DELIM|^|DELIM|^".replace("|DELIM|", DELIMITER), 3))

        test_data.append(("3|DELIM|!|DELIM|!".replace("|DELIM|", DELIMITER), 720))
        test_data.append(("1|DELIM|!|DELIM|!|DELIM|!".replace("|DELIM|", DELIMITER), 1))
        test_data.append(("2|DELIM|!|DELIM|!|DELIM|!".replace("|DELIM|", DELIMITER), 2))

        test_data.append(("2|DELIM|%|DELIM|%".replace("|DELIM|", DELIMITER), 0.0002))
        test_data.append(("3|DELIM|%|DELIM|%".replace("|DELIM|", DELIMITER), 0.0003))
        test_data.append(("0|DELIM|%|DELIM|%".replace("|DELIM|", DELIMITER), 0))

        # Tests with combination of operators
        test_data.append(("2|DELIM|3|DELIM|4|DELIM|+|DELIM|-".replace("|DELIM|", DELIMITER), -5))
        test_data.append(("2|DELIM|3|DELIM|4|DELIM|+|DELIM|-".replace("|DELIM|", DELIMITER), -5))
        test_data.append(("2|DELIM|3|DELIM|4|DELIM|+|DELIM|-".replace("|DELIM|", DELIMITER), -5))
        test_data.append(("2|DELIM|3|DELIM|+|DELIM|5|DELIM|-".replace("|DELIM|", DELIMITER), 0))
        test_data.append(("2.5|DELIM|3|DELIM|+".replace("|DELIM|", DELIMITER), 5.5))
        test_data.append(("2|DELIM|!".replace("|DELIM|", DELIMITER), 2))
        test_data.append(("123.456|DELIM|%".replace("|DELIM|", DELIMITER), 1.23456))
        test_data.append(("1|DELIM|%".replace("|DELIM|", DELIMITER), 0.01))
        test_data.append(("6|DELIM|2|DELIM|*|DELIM|3|DELIM|/".replace("|DELIM|", DELIMITER), 4))
        test_data.append(("2|DELIM|3|DELIM|^|DELIM|4|DELIM|5|DELIM|+|DELIM|+".replace("|DELIM|", DELIMITER), 17))
        test_data.append(("50|DELIM|%|DELIM|2|DELIM|*".replace("|DELIM|", DELIMITER), 1))
        test_data.append(("3|DELIM|!|DELIM|4|DELIM|5|DELIM|*|DELIM|+".replace("|DELIM|", DELIMITER), 26))
        test_data.append(("9|DELIM|3|DELIM|/|DELIM|!".replace("|DELIM|", DELIMITER), 6))
        test_data.append(
            ("5|DELIM|1|DELIM|2|DELIM|+|DELIM|4|DELIM|*|DELIM|+|DELIM|3|DELIM|-".replace("|DELIM|", DELIMITER), 14))
        test_data.append(("2|DELIM|3|DELIM|+".replace("|DELIM|", DELIMITER), 5))

        # Test for error scenarios
        test_data.append(("2|DELIM|+".replace("|DELIM|", DELIMITER), INVALID_EXPRESSION_ERROR))
        test_data.append(("*|DELIM|+".replace("|DELIM|", DELIMITER), INVALID_EXPRESSION_ERROR))
        test_data.append(("2|DELIM|3|DELIM|+|DELIM|-".replace("|DELIM|", DELIMITER), INVALID_EXPRESSION_ERROR))
        test_data.append(("1|DELIM|2|DELIM|3.4".replace("|DELIM|", DELIMITER), INVALID_EXPRESSION_ERROR))
        test_data.append(("".replace("|DELIM|", DELIMITER), INVALID_EXPRESSION_ERROR))
        test_data.append(("+".replace("|DELIM|", DELIMITER), INVALID_EXPRESSION_ERROR))
        test_data.append(("A".replace("|DELIM|", DELIMITER), NOT_A_VALID_OPERATOR))
        test_data.append(("+|DELIM|-".replace("|DELIM|", DELIMITER), INVALID_EXPRESSION_ERROR))
        test_data.append(("5|DELIM|0|DELIM|/".replace("|DELIM|", DELIMITER), DIVIDE_BY_ZERO_ERROR))
        test_data.append(("123.456|DELIM|!".replace("|DELIM|", DELIMITER), UNSUPPORTED_OPERATION_ERROR))

        return test_data


class TestRPN(object):
    @pytest.mark.parametrize('expression, expected_response', TestDataProvider.get_parameterized_test_data())
    def test_binary_operations(self, expression, expected_response):
        actual_response = RPNCalculator(expression).evaluate_rpn()
        assert actual_response == expected_response
