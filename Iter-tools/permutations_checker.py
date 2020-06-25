# To check the usage of the permutations lib from the itertool

from itertools import permutations

def permutation_checker(first_list):
    result = permutations(first_list)
    return list(result)

if __name__ == "__main__":
    first_list = [1, 2, 3]
    result = permutation_checker(first_list)
    print(result)