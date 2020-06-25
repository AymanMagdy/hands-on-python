# To check the usage of the combinations and with_replacemnt lib from the itertool

from itertools import combinations, combinations_with_replacement

def combinations_checker(first_list):
    result = combinations(first_list, 2)
    return list(result)

def combinations_with_replacement_method(first_list, replace):
    result = combinations_with_replacement(first_list, replace)
    return list(result)

if __name__ == "__main__":
    first_list = [1, 2, 3]
    replace = int(input("Enter value for the replacement: "))
    result = combinations_with_replacement_method(first_list, replace)
    print(result)