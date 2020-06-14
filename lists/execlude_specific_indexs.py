# Write a func to print a specified list after removing the 0th, 4th and 5th elements
def excludeIndexs(listElements):
    return listElements[1:4] + listElements[6:]

if __name__ == "__main__":
    sampleList = [1, 2, 4, 0, 5, 8, 9, 10]
    result = excludeIndexs(sampleList)
    print(result)