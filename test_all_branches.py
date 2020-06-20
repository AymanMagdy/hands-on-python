import os
import unittest

class TestAllBranches(unittest.TestCase):
    # Run the tests for the Dictionary branch
    def test_module_dictionary():
        os.system("nosetests Dictionary/test_dictionary_actions.py -v")

    # Run the tests for the lists branch
    def test_module_lists():
        os.system("nosetests lists/")

    # Run the tests for the tuplpes branch
    def test_module_lists():
        os.system("nosetests tuples/")
    
