# Write a func to covnert tuple to string

def convTupleToString(tupleSample):
    try:
        return ''.join(tupleSample)
    except:
        return "Error with the conversion.\nCheck the tuple's element."

if __name__ == "__main__":
    firstTuple = ('ay', 'man' )
    concatenatedTuples = convTupleToString(firstTuple)
    print(concatenatedTuples)