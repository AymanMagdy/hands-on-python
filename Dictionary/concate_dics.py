# Write a function that concates 2 given dictionaries;

def concateDictionaries(firstSampleDictionary, secondSampleDictionary):
    firstSampleDictionary.update(secondSampleDictionary)
    return firstSampleDictionary

    
if __name__ == "__main__":
    firstSampleDictionary = {'Name': 'Ayman', 'Age': 15, 'Postcode': 14554, 'State': 'MA'}
    secondSampleDictionary = {'Name1': 'Eslam', 'Age1': 18, 'Postcode1': 149954, 'State1': 'CA'}
    conatenatedDictionary = concateDictionaries(firstSampleDictionary, secondSampleDictionary)
    print(conatenatedDictionary)