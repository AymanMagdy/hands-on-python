# Write a program to create a colone of a given tuple.
from copy import deepcopy

def coloneTuple(tupleElements):
    tempTuple = deepcopy(tupleElements)
    tempTuple[2].append(12)
    return tempTuple

if __name__ == "__main__":
    sampleTuple = ('Ayan', 15, [], 'Ahmed')
    coloneTuple = coloneTuple(sampleTuple)
    print(coloneTuple)