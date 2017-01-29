import pytest
from main import RPNCalculator, ERROR


class TestDataProvider(object):
    @staticmethod
    def get_parameterized_test_data():
        test_data = list([])
        # boundary
        test_data.append(("5,0,/", ERROR))
        test_data.append(("123.456,!", ERROR))
        test_data.append(("0,!", 1))
        # inverse
        test_data.append(("5,2,-", 3))
        test_data.append(("5,3,-", 2))
        test_data.append(("5,3,*", 15))
        test_data.append(("15,3,/", 5))
        # cross check
        test_data.append(("1,2,3,+,+", 6))
        test_data.append(("1,3,2,+,+", 6))
        test_data.append(("2,1,3,+,+", 6))
        test_data.append(("2,3,1,+,+", 6))
        test_data.append(("3,2,1,+,+", 6))
        test_data.append(("3,1,2,+,+", 6))

        test_data.append(("1,2,3,-,-", 2))
        test_data.append(("1,3,2,-,-", 0))
        test_data.append(("2,1,3,-,-", 4))
        test_data.append(("2,3,1,-,-", 0))
        test_data.append(("3,2,1,-,-", 2))
        test_data.append(("3,1,2,-,-", 4))

        test_data.append(("1,2,3,*,*", 6))
        test_data.append(("1,3,2,*,*", 6))
        test_data.append(("2,1,3,*,*", 6))
        test_data.append(("2,3,1,*,*", 6))
        test_data.append(("3,2,1,*,*", 6))
        test_data.append(("3,1,2,*,*", 6))

        test_data.append(("1,2,4,/,/", 2))
        test_data.append(("1,4,2,/,/", 0.5))
        test_data.append(("2,1,4,/,/", 8))
        test_data.append(("2,4,1,/,/", 0.5))
        test_data.append(("4,2,1,/,/", 2))
        test_data.append(("4,1,2,/,/", 8))

        test_data.append(("1,2,3,^,^", 1))
        test_data.append(("1,3,2,^,^", 1))
        test_data.append(("2,1,3,^,^", 2))
        test_data.append(("2,3,1,^,^", 8))
        test_data.append(("3,2,1,^,^", 9))
        test_data.append(("3,1,2,^,^", 3))

        test_data.append(("3,!,!", 720))
        test_data.append(("1,!,!,!", 1))
        test_data.append(("2,!,!,!", 2))

        test_data.append(("2,%,%", .0002))
        test_data.append(("3,%,%", .0003))
        test_data.append(("0,%,%", 0))

        test_data.append(("2,3,4,+,-", -5))
        test_data.append(("2,3,4,+,-", -5))
        test_data.append(("2,3,4,+,-", -5))
        test_data.append(("2,3,+,5,-", 0))
        test_data.append(("2.5,3,+", 5.5))
        test_data.append(("2,!", 2))
        test_data.append(("123.456,%", 1.23456))
        test_data.append(("1,%", 0.01))
        test_data.append(("6,2,*,3,/", 4))
        test_data.append(("2,3,^,4,5,+,+", 17))
        test_data.append(("50,%,2,*", 1))
        test_data.append(("3,!,4,5,*,+", 26))
        test_data.append(("9,3,/,!", 6))
        test_data.append(("5,1,2,+,4,*,+,3,-", 14))
        test_data.append(("2,3,+", 5))
        # error
        test_data.append(("2,+", ERROR))
        test_data.append(("*,+", ERROR))
        test_data.append(("2,3,+,-", ERROR))
        test_data.append(("1,2,3.4", ERROR))
        test_data.append(("", ERROR))
        test_data.append(("+", ERROR))
        test_data.append(("34", 34))
        test_data.append(("A", ERROR))
        test_data.append(("4.33", 4.33))
        test_data.append(("+,-", ERROR))

        return test_data


class TestRPN(object):
    @pytest.mark.parametrize('expression, expected_response', TestDataProvider.get_parameterized_test_data())
    def test_binary_operations(self, expression, expected_response):
        actual_response = RPNCalculator(expression).evaluate_rpn()
        assert actual_response == expected_response
