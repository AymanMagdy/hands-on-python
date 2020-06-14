# Write a func to add an element to a tuple.

def add_to_tuple(tupleElements, newElement):
    resultTuple = (*tupleElements, newElement)
    return resultTuple

if __name__ == "__main__":
    testTuple = ('ayman', 45 )
    newValue = input("Enter a new value to add to tuple: ")
    newTuple = add_to_tuple(testTuple, newValue)
    print(newTuple)