import unittest
from common_items import commonItems
from execlude_specific_indexs import excludeIndexs
from if_one_common import isThereCommonValue
from mul_list import mulList
from rm_even_numbers import rmEvenNumbers
from smallest_largest import smallestLargest
from specific_index import specificIndex
from string_counter import stringCounterMatcher
from sum_list import sumList

# The class that includes all the test methods for the lists folder
class TestList(unittest.TestCase):
    # Testing the common_items.py
    def test_common_items(self):
        firstList = ['name', 'person', 'mr', 'cst']
        secondList = ['cst', 'eslam', 'ayman', 'name']
        try:
             self.assertEqual(commonItems(firstList, secondList), ['name', 'cst'] ,"Should return name cst")
        except Exception:
            raise AssertionError("Error with common_items(firstList, secondList)")

    # Testing the exclude_specific_index.py
    def test_exclude_specific_index(self):
        sampleList = [1, 2, 4, 0, 5, 8, 9, 10]
        try:
            self.assertEqual(excludeIndexs(sampleList), [2, 4, 0, 9, 10], "Should return [2, 4, 0, 9, 10]")
        except Exception:
            raise AssertionError("Error with exclude_specific_index(sampleList)")

    # Test the if_one_common.py
    def test_if_one_common(self):
        firstList = [1, 2, 5, 9]
        secondList = [2, 0, 8]
        try:
            self.assertEqual(isThereCommonValue(firstList, secondList), True, "Should return True")
        except Exception as error:
            raise AssertionError("Error with if_one_common(firstList, secondList)")

    # Test the mul_list.py
    def test_mul_list(self):
        listValues = [1, 2, 4]
        try:
            self.assertEqual(mulList(listValues), 8,"Should return 8.")
        except Exception as error:
            raise AssertionError("Error with if_one_common(firstList, secondList)")
    
    # Test the rm_even_numbers.py
    def test_rm_even_numbers(self):
        listSample = [1, 3, 5, 8, 10]
        try:
            self.assertEqual(rmEvenNumbers(listSample), [1, 3, 5] ,"should return [1, 3, 5]")
        except Exception as error:
            raise AssertionError("Error with rm_common_values(rmEvenNumbers)")

    # Test the smallest_largest.py
    def test_smallest_largest(self):
        listElements = [4, 5 , 3, 5]
        expected_result = {
            'smallest': 3,
            'largest': 5
        }
        try:
           self.assertEqual(smallestLargest(listElements), expected_result,"should return [3, 5]")
        except Exception as error:
            raise AssertionError("Error with smallestLargest(listSample)")

    # Test the specific_index.py
    def test_specific_index(self):
        listSample = [1, 3, 5, 8, 10]
        index = 4
        try:
           self.assertEqual(specificIndex(listSample, index), 10,"should return 10")
        except Exception as error:
            raise IndexError("Error with specific_index(sample_list)")

    # Test string_counter.py 
    def test_string_counter(self):
        sampleList = ['abc', 'xyz', 'aba', '1221']
        try:
            self.assertEqual(stringCounterMatcher(sampleList), ['aba', '1221'],"should return aba, 1221")
        except Exception as error:
            raise AssertionError("Error with specific_index(sample_list)")

    # Test sum_list.py
    def test_sum_list(self):
        sample_list = [1, 2, 3]
        try:
            self.assertEqual(sumList(sample_list), 6,"should return 6")
        except Exception as error:
            raise AssertionError("Error with sumList(sample_list)")