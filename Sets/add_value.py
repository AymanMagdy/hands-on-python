# Write a func that adds a new value to a given set.

def add_value(given_set, new_value):
    
    if given_set.__contains__(int(new_value)):
        raise AttributeError("The value already in the set.")
        return False
    else:
        given_set.add(int(new_value))
        print("The value was added to the set successfully!")
        return given_set

if __name__ == "__main__":
    sample_set = {1, 3, 4, 7}
    user_input = input("Enter a new to add to the set: ")
    print(add_value(sample_set, user_input))
    