# Write a func that checks the number of apperance of an item a given dequeque
import collections
from collections import deque

def apperance_checker(de, number_to_check):
    dequeque = deque(de)
    result = dequeque.count(number_to_check)
    return result

if __name__ == "__main__":
    de = collections.deque([3,2,2,4])
    number_to_check = int(input("Enter a number to check in the dequeque: "))
    result = apperance_checker(de, number_to_check)
    print(result)