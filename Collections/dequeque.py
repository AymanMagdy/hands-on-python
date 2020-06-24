# Write a func that creates a dequeque and iterates through the dequequq

import collections

def create_dequeque(de):
    result = ""
    for element in de:
        result += str(element)
    return int(result)


if __name__ == "__main__":
    de = collections.deque([1,2,3,4])
    result = create_dequeque(de)
    print(result)