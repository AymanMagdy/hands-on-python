import unittest
from add_to_tuple import add_to_tuple
from concate_tuples import concateTuples
from conv_tuple_srting import convTupleToString
from element_checker import isExist
from reverse_tuple import ReverseTuple

class TestTuples(unittest.TestCase):
    # Testing the first file: tuples/add_to_tuples.py
    def test_add_to_tuples(self):
        tupleElements =  ('ayman', 45 )
        newElement = 3
        self.assertEqual(add_to_tuple(tupleElements, str(newElement)), ('ayman', 45, '3') , "Should be ('ayman', 45, '3') ")

    # Tesing the concate_tuples.py
    def test_concate_tuples(self):
        firstTuple = ('ayman', 45 )
        secondTuple = ('Ahmed', 15 )
        self.assertEqual(concateTuples(firstTuple, secondTuple), ('ayman', 45, 'Ahmed', 15), "Error getting the concate of 2 tuples.")

    # Testing the conv_tuple_string.py
    def test_conv_tuple_string(self):
        firstTuple = ('ay', 'man' )
        self.assertEqual(convTupleToString(firstTuple), "ayman" , "Should return ayman")

    # Testing the element_checker.py
    def test_element_checker(self):
        sampleTuple = ('Ayan', 15, 'Ahmed')
        check = "Ayan"
        self.assertEqual(isExist(sampleTuple, check), True ,"Should return True")

    # Testing the revers_tuple.py
    def test_reverse_tuple(self):
        sampleTuple = (1, 9, 8, 7, 0)
        self.assertEqual(ReverseTuple(sampleTuple), (0, 7, 8, 9, 1) , "Should return (0, 7, 8, 9, 1)")

    # Here is to contintue testing the rest of the files.
if __name__ == '__main__':
    TestTuples.test_add_to_tuples()
    TestTuples.test_concate_tuples()
    TestTuples.test_conv_tuple_string()
    TestTuples.test_element_checker()
    TestTuples.test_reverse_tuple()