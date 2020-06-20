# write 2 functions that to return the smallest and the largest elements in a list.

# Function for the smallest number
def smallestNumber(listElements):
    smallest = listElements[0]
    for element in listElements:
        if element < smallest:
            smallest = element
    return smallest

# Function for the largest number.
def largestNumber(listElements):
    largest = listElements[0]
    for element in listElements:
        if element > largest:
            largest = element
    return largest

# To return both results directly
def smallestLargest(listElements):
    smallest = smallestNumber(listElements)
    largest = largestNumber(listElements)
    result = {
        'smallest': smallest,
        'largest': largest
    }
    return result

if __name__ == "__main__":
    listElements = [4, 5 , 3, 5]
    # To replace with the needed function.
    smallestLargestResult = smallestLargest(listElements)
    print("The smallest is: {}".format(smallestLargestResult['smallest']))
    print("The largest is: {}".format(smallestLargestResult['largest']))