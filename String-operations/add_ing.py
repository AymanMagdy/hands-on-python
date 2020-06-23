# Weite a func that adds 'ing' to the end of a given word.

def add_verb_ing(given_word):
    return given_word+'ing'


if __name__ == "__main__":
    user_string_input = str(input("Enter the needed word to add ing to: "))
    result = add_verb_ing(user_string_input)
    print("The word: {}".format(result))