# Write a func that returns min and max elements of a set

def min_max(given_set):
    min = next(iter(given_set))
    max = next(iter(given_set))
    # Getting the min value.
    for element in given_set:
        if element < min:
            min = element
    # Getting the max value.
    for element in given_set:
        if element > max:
            max = element
    
    result = {
        'min': min,
        'max': max
    }
    
    return result
        

# Wroting the main func here.
if __name__ == "__main__":
    sample_set = {1, 3, 4, 7}
    print(min_max(sample_set))