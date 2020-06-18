# write a program to unpack a tuple in different vars
def unpack_tuple(sampleTuple):
    firstVar = sampleTuple[0]
    secondVar = sampleTuple[1]

    return firstVar, secondVar

if __name__ == "__main__":
    testTuple = ('ayman', 45)
    unpacking_test_tuple = unpack_tuple(testTuple)
    print(unpacking_test_tuple)