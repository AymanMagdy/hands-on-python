# Write a simple fucntion that takes a list and mul all the elements in the list.
# The function to mul the list.
def mulList(listElemets):
    sum = 1
    for element in listElemets:
        sum *= element
    return sum

# The main function.
if __name__ == "__main__":
    listValues = [1, 2, 4]
    mulResult = mulList(listValues)
    print("The mul result: {}".format(mulResult))