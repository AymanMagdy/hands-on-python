# Write a func that iterates over a collection as many as it counts.

from collections import Counter

def counter_iterator(given_string):
    my_counter = Counter(given_string)
    result = ""
    print(my_counter.most_common())
    print("Print the elements: ")
    for element in my_counter.elements():
        result += element
    return result

if __name__ == "__main__":
    test_string = 'aaaaabbbcccc'
    result = counter_iterator(test_string)
    print(result)