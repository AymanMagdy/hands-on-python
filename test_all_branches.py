import os
import unittest

class TestAllBranches(unittest.TestCase):
    # Run the tests for the Dictionary module
    def test_module_dictionary(self):
        try:
            os.system("nosetests Dictionary/test_dictionary_actions.py -v")
        except Exception:
            raise ModuleNotFoundError("Error finding module to run test cases.")

    # Run the tests for the lists module
    def test_module_lists(self):
        try:
            os.system("nosetests lists/test_list_actions.py -v")
        except Exception:
            raise ModuleNotFoundError("Error finding module to run test cases.")

    # Run the tests for the tuplpes module
    def test_module_tuples(self):
        try:
            os.system("nosetests tuples/test_tuple_actions.py -v")
        except Exception:
            raise ModuleNotFoundError("Error finding module to run test cases.")
    
