# Write a func that multiplies all values of a given dictionary.

def mulDictionary(sampleDictionary):
    result = 1
    for key in sampleDictionary:
        result *= sampleDictionary[key]
    return result


if __name__ == "__main__":
    sampleDictionary = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 1}
    sumResult = mulDictionary(sampleDictionary)
    print(sumResult)