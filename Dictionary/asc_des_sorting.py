# Write a func to sort (asc and des) a gived dictionary by value.
import operator

def sortAsc(sampleDictionary):
    sortedDictionary = sorted(sampleDictionary.items())
    return sortedDictionary

def sortDes(sampleDictionary):
    sortedDictionary = {}
    sortedDictionary = sorted(sampleDictionary.items())
    return reversed(sortedDictionary)

if __name__ == "__main__":
    dictionaryToSort = {1:1, 7:7, 2:2, 3:3, 8:8}
    sortedAscDictionary = sortAsc(dictionaryToSort)
    sortedDesDictionary = sortDes(dictionaryToSort)
    print("Sorted Asc: {}".format(sortedAscDictionary))
    print("Sorted Des: {}".format(sortedDesDictionary))

    