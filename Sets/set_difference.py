# Write a func that creates a set difference

def set_difference(first_set, second_set):
    set_difference_result = first_set.difference(second_set)
    return set_difference_result

if __name__ == "__main__":
    first_set = {5, 3, 4, 7}
    second_set = {1, 3, 8, 7}
    print(set_difference(first_set, second_set))