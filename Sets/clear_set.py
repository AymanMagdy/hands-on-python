# Write a fun to clear a set

def clear_set(given_set):
    try:
        return given_set.clear()
    except Exception:
        raise BufferError("Error clearing the givin set.")


if __name__ == "__main__":
    sample_set = {1, 3, 4, 7}
    clear_set(sample_set)