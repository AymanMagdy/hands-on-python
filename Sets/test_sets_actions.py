import unittest
from loop_set import loop_sets
from add_value import add_value
from remove_item import remove_item
from set_difference import set_difference
from is_sub_set import is_sub_set
from clear_set import clear_set
from frozen_set import frozen_set
from set_length import set_length
from min_max import min_max

class TestSets(unittest.TestCase):
    # Testing the loop_set.py
    def test_loop_set(self):
        sample_set = {1, 3, 4, 7}
        expected_result = sample_set
        try:
            self.assertEqual(loop_sets(sample_set), expected_result, "Should return {1, 3, 4, 7}")
        except Exception:
            raise AssertionError("Error with --> loop_set.py -> test_loop(sample_set).")

    # Testing the add_value.py
    def test_add_value(self):
        sample_set = {1, 3, 4, 7}
        expected_result = {1, 3, 4, 7, 8}
        try:
            self.assertEqual(add_value(sample_set, 8), expected_result, "Should return {1, 3, 4, 7, 8}")
        except Exception:
            raise AssertionError("Error with --> add_value.py -> add_value(sample_test, new_value).")

    # Testing remove_item.py
    def test_remove_item(self):
        sample_set = {1, 3, 4, 7}
        expected_result = {3, 4, 7}
        try:
            self.assertEqual(remove_item(sample_set, 1), expected_result, "Should return {3, 4, 7}")
        except Exception:
            raise AssertionError("Error with --> remove_item.py -> remove_item(sample_test, item_to_remove).")

    # Testing set_difference.py
    def test_set_difference(self):
        first_set = {5, 3, 4, 7}
        second_set = {1, 3, 8, 7}
        expected_result = {4, 5}
        try:
            self.assertEqual(set_difference(first_set, second_set), expected_result, "Should return {4, 5}")
        except Exception:
            raise AssertionError("Error with --> set_difference.py -> set_difference(first_set, second_set).")

    # Testing is_sub_set.py
    def test_is_sub_set(self):
        first_set = {1, 2, 3}
        second_set = {9, 8, 3, 2, 1}
        try:
            self.assertEqual(is_sub_set(first_set, second_set), True, "Should return True")
        except Exception:
            raise AssertionError("Error with --> is_sub_set.py -> is_sub_set(first_set, second_set).")

    # Testing clear_set.py
    def test_clear_set(self):
        sample_set = {1, 3, 4, 7}
        try:
            self.assertEqual(clear_set(sample_set), None, "Should return None")
        except Exception:
            raise AssertionError("Error with --> is_sub_set.py -> is_sub_set(first_set, second_set).")
        
    # Testing frozen_set.py
    def test_frozen_set(self):
        sample_set = {1, 3, 4, 7}
        expected_result = frozenset({1, 3, 4, 7})
        try:
            self.assertEqual(frozen_set(sample_set), expected_result, "Should return frozenset({1, 3, 4, 7})")
        except Exception:
            raise AssertionError("Error with --> frozen_set.py -> frozen_set(sample_set).")

    # Testing set_length.py 
    def test_set_length(self):
        sample_set = {1, 3, 4, 7}
        expected_result = len(sample_set)
        try:
            self.assertEqual(set_length(sample_set), expected_result, "Should return 4)")
        except Exception:
            raise AssertionError("Error with --> set_length.py -> set_length(sample_set).")

     # Testing min_max.py {'min': 1, 'max': 7}
    def test_min_max(self):
        sample_set = {1, 3, 4, 7}
        expected_result = {'min': 1, 'max': 7}
        try:
            self.assertEqual(min_max(sample_set), expected_result, "Should return {'min': 1, 'max': 7})")
        except Exception:
            raise AssertionError("Error with --> min_max.py -> min_max(sample_set).")