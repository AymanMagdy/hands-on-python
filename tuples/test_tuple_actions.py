import unittest
from add_to_tuple import add_to_tuple
from concate_tuples import concateTuples
from conv_tuple_srting import convTupleToString
from element_checker import isExist
from reverse_tuple import ReverseTuple
from tuple_colone import coloneTuple
from tuple_to_string import to_string
from unpack_tuple import unpack_tuple
from value_index import valueIndex

class TestTuples(unittest.TestCase):
    # Testing the first file: tuples/add_to_tuples.py
    def test_add_to_tuples(self):
        tupleElements =  ('ayman', 45 )
        newElement = 3
        try:
            self.assertEqual(add_to_tuple(tupleElements, str(newElement)), ('ayman', 45, '3') , "Should be ('ayman', 45, '3') ")
        except Exception as error:
            raise error.AssertionError

    # Tesing the concate_tuples.py
    def test_concate_tuples(self):
        firstTuple = ('ayman', 45 )
        secondTuple = ('Ahmed', 15 )
        try:
            self.assertEqual(concateTuples(firstTuple, secondTuple), ('ayman', 45, 'Ahmed', 15), "Error getting the concate of 2 tuples.")
        except Exception as error:
            raise error.AssertionError

    # Testing the conv_tuple_string.py
    def test_conv_tuple_string(self):
        firstTuple = ('ay', 'man' )
        try:
            self.assertEqual(convTupleToString(firstTuple), "ayman" , "Should return ayman")
        except Exception as error:
            raise error.AssertionError

    # Testing the element_checker.py
    def test_element_checker(self):
        sampleTuple = ('Ayan', 15, 'Ahmed')
        check = "Ayan"
        try:
            self.assertEqual(isExist(sampleTuple, check), True ,"Should return True")
        except Exception as error:
            raise error.AssertionError

    # Testing the revers_tuple.py
    def test_reverse_tuple(self):
        sampleTuple = (1, 9, 8, 7, 0)
        try:
            self.assertEqual(ReverseTuple(sampleTuple), (0, 7, 8, 9, 1) , "Should return (0, 7, 8, 9, 1)")
        except Exception as error:
            raise error.AssertionError

    # Testing the tuple_colone.py
    def test_colone_tuple(self):
        sampleTuple = ('Ayan', 15, [], 'Ahmed')
        try:
            self.assertEqual(coloneTuple(sampleTuple), ('Ayan', 15, [12], 'Ahmed'), "Should return ('Ayan', 15, [12], 'Ahmed')")
        except Exception as error:
            raise error.AssertionError

    # Testing the tuple_to_string.py
    def test_tuple_to_string(self):
        sampleTuple = (1, 9, 8, 7, 0)
        try:
            self.assertEqual(to_string(sampleTuple), str((1, 9, 8, 7, 0)), "Should return (1, 9, 8, 7, 0)")
        except Exception as error:
            raise error.AssertionError

    # Testing the unpack_tuple.py
    def test_unpack_tuple(self):
        sample_tuple = ('ayman', 45)
        try:
            self.assertEqual(unpack_tuple(sample_tuple), ('ayman', 45), "Should return ('ayman', 45)")
        except Exception as error:
            raise error.AssertionError

    # Tesing the value_index.py
    def test_value_index(self):
        sample_tuple = ('Ayan', 15, 'Ahmed')
        value_to_check = 15
        try:
            self.assertEqual(valueIndex(sample_tuple, str(value_to_check)), (True, 9), "Should return False.")
        except Exception as error:
            raise error.AssertionError

if __name__ == '__main__':
    TestTuples.test_add_to_tuples()
    TestTuples.test_concate_tuples()
    TestTuples.test_conv_tuple_string()
    TestTuples.test_element_checker()
    TestTuples.test_reverse_tuple()
    TestTuples.test_colone_tuple()
    TestTuples.test_tuple_to_string()