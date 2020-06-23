# write a fun that returns the number of the comma sep in a fiven string

def comma_counter(given_word):
    result_comma_number = 0
    for char in given_word:
        if char == ',':
            result_comma_number += 1
    return result_comma_number

if __name__ == "__main__":
    given_string = "hello, python progra, how, are, you"
    print(comma_counter(given_string))