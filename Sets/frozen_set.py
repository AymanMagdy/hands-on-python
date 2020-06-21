# Write a func that creats a frozen set

def frozen_set(given_set):
    try:
        frozen_set_obj = frozenset(given_set)
        return frozen_set_obj
    except Exception:
        raise AttributeError("Error intializing the frozonset object") 

# Wroting the main func here.
if __name__ == "__main__":
    sample_set = {1, 3, 4, 7}
    print(frozen_set(sample_set))