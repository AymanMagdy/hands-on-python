# Write a func that retuns the unique values in a gives dictionary.

def unique_values(list_dics):
    l_unique_values = set(value for dictionary in list_dics for value in dict.values())
    return l_unique_values

if __name__ == "__main__":
    sampleDictionary = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    result = unique_values(sampleDictionary)
    print("The unique values: {}".format(result))