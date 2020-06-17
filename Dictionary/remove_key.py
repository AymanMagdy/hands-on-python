# Write a func that removes a key from a given dictionary

# The function for removing the key and sending a response to the user.
def removeKey(sampleDictionary, keyToRemove):
    try:
        del sampleDictionary[keyToRemove]
        response = {
            'status': True,
            'code': 200,
            'dictionary': sampleDictionary
        }
        return response
    except:
        response = {
            'status': False,
            'code': 400
        }
        return response

if __name__ == "__main__":
    sampleDictionary = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 1}
    keyToRemove = input('Enter the key to be removed: ')
    rmResult = removeKey(sampleDictionary, keyToRemove)
    if rmResult['status'] == True:
        print('The key has been removed successfully!')
        print("The dictionary after the removal process: {}".format(rmResult['dictionary']))
    elif rmResult['status'] == False:
        print('Error removing the key from the given dictionary.')