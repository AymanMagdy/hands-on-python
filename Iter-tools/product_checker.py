# Checking the functions and the usage of the itertools, Products, Permutation, combinations, accumulate, groupby, and infinite interators

from itertools import product

def product_checker(first_list, second_list):
    prod_a = product(first_list, second_list)
    return list(prod_a)

if __name__ == "__main__":
    first_list = [1, 2]
    second_list = [5, 6]
    result = product_checker(first_list, second_list)
    print(result)

