# Write a func that sorts a tuple using lambda

def sort_tuple(given_tuple):
    sorting_lambda = lambda given_tuple: sorted(given_tuple)
    return sorting_lambda(given_tuple)

if __name__ == "__main__":
    test_tuple = (2, 1, 5, 4, 7, 8)
    result = sort_tuple(test_tuple)
    print(result)