# Write a func that tests if that checks if a set is a subset of another set

def is_sub_set(first_set, second_set):
    result = first_set.issubset(second_set)
    if result is True:
        return True
    else:
        return False

if __name__ == "__main__":
    first_set = {1, 2, 3}
    second_set = {9, 8, 3, 2, 1}
    print(is_sub_set(first_set, second_set))