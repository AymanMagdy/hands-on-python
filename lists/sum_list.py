# Write a simple fucntion that takes a list and sum all the elements in the list.
# The function to sum the list.
def sumList(listElemets):
    sum = 0
    for element in listElemets:
        sum += element
    return sum

# The main function.
if __name__ == "__main__":
    listValues = [1, 2, 3]
    sumResult = sumList(listValues)
    print("The sum result: {}".format(sumResult))
