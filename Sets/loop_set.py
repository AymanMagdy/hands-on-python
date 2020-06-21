# Write a func that would iterate over sets

def loop_sets(set_items):
    for item in set_items:
        print("Item: {}".format(item))
    return set_items

if __name__ == "__main__":
    sample_set = {1, 3, 4, 7}
    loop_result = loop_sets(sample_set)