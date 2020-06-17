# Write a func that returns the min and the max values in a dictionary.

def getMinValue(dictionary):
    # To get the first value of the dictionary, { get the values, make an iterator to the values iter(values), point to the first value with next(value_iterator)}
    values = dictionary.values()
    value_iterator = iter(values)
    small = next(value_iterator)
    for value in values:
        if value < small:
            small = value
    return small

def getMaxValue(dictionary):    # To get the first value of the dictionary, { get the values, make an iterator to the values iter(values), point to the first value with next(value_iterator)}

    # To get the first value of the dictionary, { get the values, make an iterator to the values iter(values), point to the first value with next(value_iterator)}
    values = dictionary.values()
    value_iterator = iter(values)
    max = next(value_iterator)
    for value in values:
        if value > max:
            max = value
    return max

def getMinMax(dictionary):
    min = getMinValue(dictionary)
    max = getMaxValue(dictionary)
    response = {
        "Min": min,
        "Max": max
    } 

    return response

if __name__ == "__main__":
    sampleDictionary = {1: 0, 2: 9, 3: 8, 4: 4}
    result = getMinMax(sampleDictionary)
    print("The min value: {}".format(result["Min"]))
    print("The max value: {}".format(result["Max"]))