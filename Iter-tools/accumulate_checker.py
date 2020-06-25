# To check the usage of the accumulate lib from the itertool

from itertools import accumulate
import operator

def accumulate_checker(first_list):
    result = accumulate(first_list, func=operator.mul)
    return list(result)


if __name__ == "__main__":
    first_list = [1, 2, 4, 3]
    print(first_list)
    result = accumulate_checker(first_list)
    print(result)