# Write a func that removes an item from a given set.

def remove_item(given_set, item_to_remove):
    if given_set.__contains__(int(item_to_remove)):
        given_set.remove(int(item_to_remove))
        return given_set
    elif not given_set.__contains__(int(item_to_remove)):
        raise AttributeError("The entered item  is not in the set.")

if __name__ == "__main__":
    sample_set = {1, 3, 4, 7}
    user_input = input("Enter a new to remove from the set: ")
    print(remove_item(sample_set, user_input))