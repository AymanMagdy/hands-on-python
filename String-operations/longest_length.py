# Write a func that gets a list of strings and return the length of the longest one

def largest_string_length(given_list):
    longest_len = len(given_list[0])
    for user_string in given_list:
        if len(user_string) > longest_len:
            longest_len = len(user_string)
    return longest_len


if __name__ == "__main__":
    user_list = ['name', 'user', 'testj']
    result = largest_string_length(user_list)
    print("The longes is: {}".format(result))