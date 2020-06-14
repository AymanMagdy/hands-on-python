# Write a function that will return a specific index's element

def specificIndex(listElements, index):
    if index >= len(listElements):
        return "Not a valid index."
    return listElements[index]

if __name__ == "__main__":
    listSample = [1, 3, 5, 8, 10]
    index = input("Enter a specific element: ")
    result = specificIndex(listSample, int(index))
    print(result)