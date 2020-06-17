# Write a func to map 2 lists into a dictionaty

def mapListsToDictionary(firstList, secondList):
    dictionaty = dict(zip(firstList, secondList))
    return dictionaty

if __name__ == "__main__":
    firstList = [1,2,3,4]
    secondList = [5,6,7,8]
    finalDictionary = mapListsToDictionary(firstList, secondList)
    print(finalDictionary)