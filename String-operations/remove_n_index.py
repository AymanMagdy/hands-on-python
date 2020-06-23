# Write a func that removes n index from an string

def remove_index(given_string, index_to_remove):
    index = 0
    final_string = ""
    for char in given_string:
        if index == index_to_remove:
            print(char)
        else:
            final_string += char
        index +=1
    return final_string

if __name__ == "__main__":
    given_string = "ayman"
    index_to_remove = 1
    print(remove_index(given_string, index_to_remove))