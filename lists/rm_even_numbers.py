# Write a func that remove the even numbers from a list
def rmEvenNumbers(listElements):
    evenNumbers = []
    for element in listElements:
        if element %2 != 0:
            evenNumbers.append(element)
    return evenNumbers

if __name__ == "__main__":
    listSample = [1, 3, 5, 8, 10]
    result = rmEvenNumbers(listSample)
    print(result)