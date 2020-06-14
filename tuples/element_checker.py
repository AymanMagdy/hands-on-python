# Write a program to check if an element exist in a tuple.

def isExist(tupleElements, valueToCheck):
    if str(valueToCheck) in str(tupleElements):
        return True
    return False

if __name__ == "__main__":
    sampleTuple = ('Ayan', 15, 'Ahmed')
    check = input('Enter a value to check: ')
    result = isExist(sampleTuple, check)
    print(result)