import unittest
from add_using_lambda import lambda_adder
from mul_using_lambda import lambda_multplier
from sort_tuple_lambda import sort_tuple

class TestLambdaActions(unittest.TestCase):
    # Testing add_using_lambda
    def test_lambda_adder(self):
        base_value = 3
        add_on = 3
        expected_result = 6
        try:
            self.assertEqual(lambda_adder(base_value, add_on), expected_result, "Should return 6")
        except: 
            raise AssertionError("Error with --> add_using_lambda.py -> lambda_adder(base_value, add_on)")

    # Testing add_using_lambda
    def test_lambda_multplier(self):
        value_x = 3
        value_y = 3
        expected_result = 9
        try:
            self.assertEqual(lambda_multplier(value_x, value_y), expected_result, "Should return 9")
        except: 
            raise AssertionError("Error with --> mul_using_lambda.py -> lambda_multplier(value_x, value_y)")

    # Testing sort_tuple_lambda.py
    def test_sort_tuple(self):
        test_tuple = (2, 1, 5, 4, 7, 8)
        expected_result = [1, 2, 4, 5, 7, 8]
        try:
            self.assertEqual(sort_tuple(test_tuple), expected_result, "Should return [1, 2, 4, 5, 7, 8]")
        except: 
            raise AssertionError("Error with --> sort_tuple_lambda.py -> sort_tuple(test_tuple)")