# Write a function that returns true if there's at least one common value in 2 lists.
def isThereCommonValue(firstList, secondList):
    for element in firstList:
        if element in secondList:
            return True
    return False

if __name__ == "__main__":
    firstList = [1, 2, 5, 9]
    secondList = [2, 0, 8]
    result = isThereCommonValue(firstList, secondList)
    print(result)