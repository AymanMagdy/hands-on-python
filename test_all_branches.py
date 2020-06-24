import os
import unittest

class TestAllBranches(unittest.TestCase):
    # Run the tests for the Dictionary module
    def test_module_dictionary(self):
        try:
            os.system("nosetests Dictionary/test_dictionary_actions.py -v")
        except Exception:
            raise ModuleNotFoundError("Error finding module to run -> Dictionary test cases.")

    # Run the tests for the lists module
    def test_module_lists(self):
        try:
            os.system("nosetests lists/test_list_actions.py -v")
        except Exception:
            raise ModuleNotFoundError("Error finding module -> lists to run test cases.")

    # Run the tests for the tuplpes module
    def test_module_tuples(self):
        try:
            os.system("nosetests tuples/test_tuple_actions.py -v")
        except Exception:
            raise ModuleNotFoundError("Error finding module -> tuples to run test cases.")
    
    # Run the tests for the Sets module
    def test_module_sets(self):
        try:
            os.system("nosetests Sets/test_sets_actions.py -v")
        except Exception:
            raise ModuleNotFoundError("Error finding module -> Sets to run test cases.")

    # Run the tests for the Sets module
    def test_module_string_operations(self):
        try:
            os.system("nosetests String-operations/test_string_operations.py -v")
        except Exception:
            raise ModuleNotFoundError("Error finding module -> String-operations to run test cases.")

    # Run the tests for the Sets module
    def test_module_Collections(self):
        try:
            os.system("nosetests Collections/test_collections_actions.py -v")
        except Exception:
            raise ModuleNotFoundError("Error finding module -> Sets to run test cases.")