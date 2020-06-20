# write a func that sums all the value in a given dictionary

def sumDictionary(sampleDictionary):
    result = 0
    for key in sampleDictionary:
        result += sampleDictionary[key]
    return result


if __name__ == "__main__":
    sampleDictionary = {'key1': 1, 'key2': 2, 'key3': 3}
    sumResult = sumDictionary(sampleDictionary)
    print(sumResult)