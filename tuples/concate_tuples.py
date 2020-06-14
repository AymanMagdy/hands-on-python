# Write a function to concate 2 tuples.

def concateTuples(firstTuple, secondTuple):
    return firstTuple + secondTuple

if __name__ == "__main__":
    firstTuple = ('ayman', 45 )
    secondTuple = ('Ahmed', 15 )
    concatenatedTuples = concateTuples(firstTuple, secondTuple)
    print(concatenatedTuples)