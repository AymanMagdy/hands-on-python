# write a func that takes a sentence and return the words of the sentence in sorted order.

def sort_words(given_sentence):
    words = given_sentence.split()
    words.sort()
    return words

if __name__ == "__main__":
    given_string = "hello python program how are you"
    print(sort_words(given_string))