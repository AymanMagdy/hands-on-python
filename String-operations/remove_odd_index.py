# remove chars with odd index

def remove_odd_indexs(given_string):
    result = ""
    index = 0
    for char in given_string:
        if index % 2 == 0:
            result += char
        index += 1
    return result

if __name__ == "__main__":
    test_string = "ayman"
    result = remove_odd_indexs(test_string)
    print(result)