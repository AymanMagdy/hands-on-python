# Write a func to make all tuple elements to string.

def to_string(tupleElments):
    print("The type is: {}".format(type(tupleElments)))
    return str(tupleElments)

if __name__ == "__main__":
    sampleTuple = (1, 9, 8, 7, 0)
    toStringTuple = to_string(sampleTuple)
    print("The type after conversion: {}".format(type(toStringTuple)))
    print(toStringTuple)


