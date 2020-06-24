# Write a func that removes all the elements in a given dqueque

import collections

def remove_element_dqueque(de):
    de = collections.deque([1,2,3,4])
    de.clear()
    return de

if __name__ == "__main__":
    de = collections.deque([1,2,3,4])
    result = remove_element_dqueque(de)
    print(result)
    # if len(result) == 0:
    #     print('Empty dequeque')
    # else:
    #     print(result)
