# write a string that will return a string from the first 2 and last 2 chars.

def get_string(given_word):
    counter = 0
    string_name_lenght = len(given_word)
    result = ""
    chars_index_result = [0, 1, string_name_lenght-1, string_name_lenght-2]
    for char in given_word:
        if counter in chars_index_result:
            result += char
        counter += 1
    return result

if __name__ == "__main__":
    user_string_input = str(input("Enter the needed word to check: "))
    result = get_string(user_string_input)
    print("The result: {}".format(result))