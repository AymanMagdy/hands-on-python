# Write a func to that returns the index of a value if exists

def valueIndex(tupleElements, valueToCheck):
    try:
        stringTupleElements = str(tupleElements)
        return stringTupleElements.index(str(valueToCheck))
    except:
        return "The element is not in the tuple."

if __name__ == "__main__":
    sampleTuple = ('Ayan', 15, 'Ahmed')
    valueToCheck = input('Enter a value to check: ')
    checkerResult = valueIndex(sampleTuple, valueToCheck)
    print(checkerResult)