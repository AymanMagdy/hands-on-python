import unittest
import collections
from collections_iterator import counter_iterator
from most_common_element import most_common_item
from least_occured import least_common_item
from dequeque import create_dequeque
from remove_elements_from_dequeque import remove_element_dqueque
from collections import deque
from chec_dequeque import apperance_checker

class TestCollectionsActions(unittest.TestCase):
    # Test the collections_iterator.py
    def test_collections_iterator(self):
        test_string = "aaaaabbbbcccc"
        expected_result = "aaaaabbbbcccc"
        try:
            self.assertEqual(counter_iterator(test_string), expected_result, "Should return 'aaaaabbbbcccc'")
        except Exception:
            raise AssertionError("Error with method collections_iterator.py -> counter_iterator(given_string)")

    # Test the collections_iterator.py
    def test_most_common_element(self):
        test_string = "aaaaabbbbcccc"
        expected_result = ('a', 5)
        try:
            self.assertEqual(most_common_item(test_string), expected_result, "Should return ' ('a', 5) '")
        except Exception:
            raise AssertionError("Error with method most_common_element.py -> most_common_element(given_string)")
    
    # Test the collections_iterator.py
    def test_least_common_element(self):
        test_string = "aaaaabbbcccc"
        expected_result = ('b', 3)
        try:
            self.assertEqual(least_common_item(test_string), expected_result, "Should return ' ('b', 3) '")
        except Exception:
            raise AssertionError("Error with method least_common_item.py -> least_common_item(given_string)")
    
    # Test the dequeque.py
    def test_create_dequeque(self):
        test_string = collections.deque([1, 3, 4, 5])
        expected_result = 1345
        try:
            self.assertEqual(create_dequeque(test_string), expected_result, "Should return 'int -> 12345 ")
        except Exception:
            raise AssertionError("Error with method create_dqueque.py -> create_dqueque()")

     # Test the remove_elements_from_dequeque.py
    def test_remove_element_dqueque(self):
        test_string = collections.deque([1, 3, 4, 5])
        expected_result = deque([])
        try:
            self.assertEqual(remove_element_dqueque(test_string), expected_result, "Should return ' deque([])' ")
        except Exception:
            raise AssertionError("Error with method remove_elements_from_dequeque.py -> remove_element_dqueque()")

    # Test the chec_dequeque.py
    def test_apperance_checker(self):
        test_string = collections.deque([1, 3, 4, 5])
        number_to_check = 3
        expected_result = 1
        try:
            self.assertEqual(apperance_checker(test_string, number_to_check), expected_result, "Should return '1' ")
        except Exception:
            raise AssertionError("Error with method chec_dequequeq.py -> apperance_checker(de, numner_to_check)")