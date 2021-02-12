# This file contains all functions pertaining to testing wordCounter.

from wordCounter import count_words

# A template for testing count_words that inputs a string to count words from
# and compares the results of the function to a dictionary you provide.
def count_words_test_template(input_str, comparison_dict):
    count_words_result = count_words(input_str)
    assert count_words_result == comparison_dict

# The specific tests for count_words.
def test_count_words_empty():
    input_str = ""
    comparison_dict = {}
    count_words_test_template(input_str, comparison_dict)

def test_count_words_blank_space():
    input_str = " \n\t"
    comparison_dict = {}
    count_words_test_template(input_str, comparison_dict)

def test_count_words_special_chars():
    input_str = "\\.!?~#$%&*"
    comparison_dict = {}
    count_words_test_template(input_str, comparison_dict)

def test_count_words_one_word():
    input_str = "Hello"
    comparison_dict = {"hello": 1}
    count_words_test_template(input_str, comparison_dict)

def test_count_words_two_words():
    input_str = "Hello world"
    comparison_dict = {"hello": 1, "world": 1}
    count_words_test_template(input_str, comparison_dict)

def test_count_words_ignore_case():
    input_str = "Hello hello"
    comparison_dict = {"hello": 2}
    count_words_test_template(input_str, comparison_dict)

def test_count_words_ignore_special_chars():
    input_str = "Hell'o hello!"
    comparison_dict = {"hello": 2}
    count_words_test_template(input_str, comparison_dict)

def test_count_words_all_splits():
    input_str = "Hello hello\nhello\thello"
    comparison_dict = {"hello": 4}
    count_words_test_template(input_str, comparison_dict)