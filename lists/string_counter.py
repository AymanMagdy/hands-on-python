# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

# The needed function.
def stringCounterMatcher(listStrings):
    matchedElements = []
    for string in listStrings:
        stringLength = len(string)
        if stringLength > 2 and (string[0] == string[stringLength-1]):
            matchedElements.append(string)
    return matchedElements

if __name__ == "__main__":
    sampleList = ['abc', 'xyz', 'aba', '1221']
    resultList = stringCounterMatcher(sampleList)
    for result in resultList:
        print(result)
