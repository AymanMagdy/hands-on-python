import unittest
from split_strings import seperate_string
from get_string import get_string
from add_ing import add_verb_ing
from lyrics_determiner import check_lyrics
from longest_length import largest_string_length
from remove_n_index import remove_index
from remove_odd_index import remove_odd_indexs
from sort_words import sort_words
from comma_sep_counter import comma_counter

class TestStringOperations(unittest.TestCase):
    # Test split_strings.py
    def test_split_strings(self):
        first_string = "ayman"
        second_string = "eslam"
        expected_result = "ayman eslam"
        try:
            self.assertEqual(seperate_string(first_string, second_string), expected_result, "Should return 'ayman eslam'")
        except Exception:
            raise AssertionError("Error with method --> split_strings.py -> sperate_string(first_string, second_string)")
    
    # Test get_string.py
    def test_get_string(self):
        test_string = "personname"
        expected_result = "peme"
        try:
            self.assertEqual(get_string(test_string), expected_result, "Should return 'peme'")
        except Exception:
            raise AssertionError("Error with method --> get_string.py -> get_string(given_word)")
    
    # Test add_ing.py
    def test_add_ing(self):
        test_string = "personname"
        expected_result = "personnameing"
        try:
            self.assertEqual(add_verb_ing(test_string), expected_result, "Should return 'personnameing'")
        except Exception:
            raise AssertionError("Error with method --> add_ing.py -> add_verrb_ing(given_word)")
    
    # Test lyrics_checker.py
    def test_lyrics_checker(self):
        test_string = "not bad"
        expected_result = "The lyrics is good!"
        try:
            self.assertEqual(check_lyrics(test_string), expected_result, "Should return 'The lyrics is good!'")
        except Exception:
            raise AssertionError("Error with method --> lyrics_checker.py -> chek_lyrics(given_user_opinion.py)")

    # Test longest_length.py
    def test_longest_string_length(self):
        test_string = ['name', 'user', 'testj']
        expected_result = 5
        try:
            self.assertEqual(largest_string_length(test_string), expected_result, "Should return '5'")
        except Exception:
            raise AssertionError("Error with method --> longest_length.py -> largets_string_lenght(given_user_opinion.py)")
    
    # Test remove_n_index.py
    def test_remove_string_index(self):
        test_string = "ayman"
        index_to_remove = 1
        expected_result = 'aman'
        try:
            self.assertEqual(remove_index(test_string, index_to_remove), expected_result, "Should return 'aman'")
        except Exception:
            raise AssertionError("Error with method --> remove_n_index.py -> remove_index(given_string, index_to_remove)")

    # Test remove_n_index.py
    def test_remove_odd_index(self):
        test_string = "ayman"
        expected_result = 'amn'
        try:
            self.assertEqual(remove_odd_indexs(test_string), expected_result, "Should return 'amb'")
        except Exception:
            raise AssertionError("Error with method --> remove_n_index.py -> remove_odd_indexs(given_string)")

    # Test sort_words.py
    def test_sort_words(self):
        test_string = "hello python program how are you"
        expected_result = ['are', 'hello', 'how', 'program', 'python', 'you']
        try:
            self.assertEqual(sort_words(test_string), expected_result, "Should return '['are', 'hello', 'how', 'program', 'python', 'you']'")
        except Exception:
            raise AssertionError("Error with method --> sort_words.py -> sort_words(given_string)")

     # Test comma_sep_number.py
    def test_comma_counter(self):
        test_string = "hello, python progra, how, are, you"
        expected_result = 4
        try:
            self.assertEqual(comma_counter(test_string), expected_result, "Should return '4'")
        except Exception:
            raise AssertionError("Error with method --> comma_sep_counter.py -> comma_conuter(given_string)")