import unittest
from asc_des_sorting import sortAsc
from concate_dics import concateDictionaries
from key_exists import isKeyExist
from map_lists_dictionary import mapListsToDictionary
from min_max_dictionary import getMinMax
from mul_dictionary import mulDictionary
from remove_key import removeKey
from sum_values import sumDictionary

class TestDictionary(unittest.TestCase):

    # Test asc_sorting
    def test_asc_sort(self):
        dictionaryToSort = {1:1, 7:7, 2:2, 3:3, 8:8}
        try:
            self.assertEqual(sortAsc(dictionaryToSort), [(1, 1), (2, 2), (3, 3), (7, 7), (8, 8)], "Should return  [(1, 1), (2, 2), (3, 3), (7, 7), (8, 8)]")
        except Exception:
            raise AssertionError("Error with sortAsc(dictionaryToSort)")

    # Test concate_dics.py
    def test_concate_dics(self):
        firstSampleDictionary = {'Name': 'Ayman', 'Age': 15, 'Postcode': 14554, 'State': 'MA'}
        secondSampleDictionary = {'Name1': 'Eslam', 'Age1': 18, 'Postcode1': 149954, 'State1': 'CA'}
        expected_result = {'Name': 'Ayman', 'Age': 15, 'Postcode': 14554, 'State': 'MA', 'Name1': 'Eslam', 'Age1': 18, 'Postcode1': 149954, 'State1': 'CA'}
        try:
            self.assertEqual(concateDictionaries(firstSampleDictionary, secondSampleDictionary), expected_result, "Should return expected_value variable")
        except Exception as error:
            raise AssertionError("Error with the method concate_dics.")

    # Test is_key_exist.py
    def test_is_key_exist(self):
        sample_dictionary = {'Name': 'Ayman', 'Age': 15, 'Postcode': 14554, 'State': 'MA'}
        key = 'Name'
        value = 'Ayman'
        expected_result = True
        try:
            self.assertEqual(isKeyExist(sample_dictionary, key, value), expected_result, "Should return True")
        except Exception as error:
            raise AssertionError("Error with the method is_key_exist(smaple_dictionary, key, value).")

    # Test map_lists_dictionary.py
    def test_map_list_dictionary(self):
        firstList = [1,2,3,4]
        secondList = [5,6,7,8]
        expected_result = {1: 5, 2: 6, 3: 7, 4: 8}
        try:
            self.assertEqual(mapListsToDictionary(firstList, secondList), expected_result, "Should return expected_result var")
        except Exception as error:
            raise AssertionError("Error with the method mapListsToDictionary(firstList, secondList).")

    # Test min_max_dictionary.py
    def test_get_min_max(self):
        sampleDictionary = {1: 0, 2: 9, 3: 8, 4: 4}
        expected_result = {
            "Min": 0,
            "Max": 9
        }
        try:
            self.assertEqual(getMinMax(sampleDictionary), expected_result, "Should return expected_result {min: 0, max: 9}")
        except Exception as error:
            raise AssertionError("Error with the method get_min_max(dictionary).")

    # Testing mul_dictionary.py
    def test_mul_dictionary(self):
        sample_dictionary =  {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 1}
        expected_result = 24
        try:
            self.assertEqual(mulDictionary(sample_dictionary), expected_result, "Should return 24")
        except Exception as error:
            raise AssertionError("Error with the method mulDictionary(firstList).")

    # Testinng remove_keys.py
    def test_remove_key(self):
        sampleDictionary = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 1}
        key_to_remove = 'key1'
        response = {
            'status': True,
            'code': 200,
            'dictionary': sampleDictionary
        }
        try:
            self.assertEqual(removeKey(sampleDictionary, key_to_remove), response , "Should return respose['status']: True")
        except Exception as error:
            raise AssertionError("Error with the method remove_key(sample_dictionary, key_to_remove).")

    # Testing sum_values.py unique_values
    def test_sum_values(self):
        sampleDictionary = {'key1': 1, 'key2': 2, 'key3': 3}
        expected_result = 6
        try:
            self.assertEqual(sumDictionary(sampleDictionary), expected_result , "Should return 6")
        except Exception as error:
            raise AssertionError("Error with the method sumDictionary(sampleDictionary).")