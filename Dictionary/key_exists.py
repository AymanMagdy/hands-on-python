# Write a func that a value and checks if that key and value exists.

def isKeyExist(dictionaySample, searchKey, searchValue):
    if searchKey in dictionarySample:
        if searchValue == str(dictionarySample[searchKey]):
            print("We have found the key matching the value.")
            return True
        print("We found the key, but the value is not matching.")
        return False
    print("We didn't find the key!")
    return False

if __name__ == "__main__":
    dictionarySample = {'Name': 'Ayman', 'Age': 15, 'Postcode': 14554, 'State': 'MA'}
    key = input("Enter the needed key:")
    value = input("Enter the value: ")
    isExit = isKeyExist(dictionarySample, key, value)
    print("Does {} with value {} in the given dicitonary exist: {}".format(key, value, isExit))