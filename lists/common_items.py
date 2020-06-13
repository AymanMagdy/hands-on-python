# write a function to find the common items in 2 lists.

def commonItems(firstList, secondList):
    commonElements = []
    for elementFirstList in firstList:
        for elementSecondtList in secondList:
            if elementFirstList == elementSecondtList:
                commonElements.append(elementFirstList)
    return commonElements

if __name__ == "__main__":
    firstList = ['name', 'person', 'mr', 'cst']
    secondList = ['cst', 'eslam', 'ayman', 'name']
    commonInLists = commonItems(firstList, secondList)
    for element in commonInLists:
        print(element)