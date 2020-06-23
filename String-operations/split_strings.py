# Write a func that takes 2 strings and brings both in string seperated with sapce.

def seperate_string(first_string, second_string):
    result = first_string + " " + second_string
    return str(result)

if __name__ == "__main__":
    first_string = "ayman"
    second_string = "eslam"
    print(seperate_string(first_string, second_string))
    