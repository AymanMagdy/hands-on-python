# Write a func that returns the most common item.

from collections import Counter

def least_common_item(given_string):
    my_counter = Counter(given_string)
    most_common = my_counter.most_common().pop()
    return most_common

if __name__ == "__main__":
    test_string = 'aaaaabbbcccc'
    result = least_common_item(test_string)
    print(result)
