# Write a func that would take a setence from the user and return the lyrics is poor or good

def check_lyrics(given_user_opinion):
    if "not" and "poor" or "bad" in given_user_opinion:
        result = "The lyrics is good!"
    else:
        result = "The lyrics is poor!"
    return result

if __name__ == "__main__":
    user_string_input = str(input("Enter your opinion about the song: "))
    result = check_lyrics(user_string_input)
    print("The word: {}".format(result))