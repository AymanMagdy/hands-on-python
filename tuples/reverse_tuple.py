# Write a func to reverse a given tuple.

def ReverseTuple(tupleElements):
    newTuple = ()
    for element in reversed(tupleElements):
        newTuple = newTuple + (element,)
    return newTuple

if __name__ == "__main__":
    sampleTuple = (1, 9, 8, 7, 0)
    reversedTuple = ReverseTuple(sampleTuple)
    print(reversedTuple)