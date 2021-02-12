# This file contains all functions pertaining to testing fileReader.

import os
import json
from fileReader import read_file

# A template for testing read_file that inputs all of the command line arguments,
# a std_out string, and json contents.  Then it compares the printed results of the
# function to the std_out string and, if a json file is made, the results of the json
# file made to the json contents.
def read_file_test_template(capsys, file_name, number_of_words_to_print, return_json, json_name, std_out_string, json_contents):
    read_file(file_name, number_of_words_to_print, return_json, json_name)
    captured = capsys.readouterr()
    assert captured.out == std_out_string
    if json_contents != None:
        try:
            json_file_name = file_name.replace(".txt", "") + "_" + json_name + ".json"
            file = open(json_file_name, "r")
            json_formatted_file_contents = json.load(file)
        except:
            assert False
        assert json_formatted_file_contents == json_contents

# The specific tests for read_file.
def test_read_file_doesnt_exist(capsys):
    file_name = ""
    number_of_words_to_print = 10
    return_json = False
    json_name = "word_counts"
    std_out_string = "An error was ecountered trying to open the file you specified.\n"
    json_contents = None
    read_file_test_template(capsys, file_name, number_of_words_to_print, return_json, json_name, std_out_string, json_contents)

def test_read_test_file_no_json(capsys):
    file_name = "test.txt"
    number_of_words_to_print = 10
    return_json = False
    json_name = "word_counts"
    std_out_string = "hello - 9\nto - 5\nof - 4\nis - 4\nhow - 3\nare - 3\nyou - 3\njimmy - 3\nmartha - 3\nsay - 3\n"
    json_contents = None
    read_file_test_template(capsys, file_name, number_of_words_to_print, return_json, json_name, std_out_string, json_contents)

def test_read_test_file_no_json_5_words(capsys):
    file_name = "test.txt"
    number_of_words_to_print = 5
    return_json = False
    json_name = "word_counts"
    std_out_string = "hello - 9\nto - 5\nof - 4\nis - 4\nhow - 3\n"
    json_contents = None
    read_file_test_template(capsys, file_name, number_of_words_to_print, return_json, json_name, std_out_string, json_contents)

def test_read_test_file_no_json_over_max_words(capsys):
    file_name = "test.txt"
    number_of_words_to_print = 1000
    return_json = False
    json_name = "word_counts"
    std_out_string = ("hello - 9\nto - 5\nof - 4\nis - 4\nhow - 3\nare - 3\nyou - 3\njimmy - 3\nmartha - 3\n"
                      "say - 3\nmyself - 2\nand - 2\nsamantha - 2\nwant - 2\nan - 2\na - 2\nsequence - 2\nworld - 1\n"
                      "as - 1\nwell - 1\nlike - 1\ntalking - 1\ntogether - 1\nsaying - 1\neachother - 1\nwants - 1\n"
                      "too - 1\nwhy - 1\ndoes - 1\neveryone - 1\nlist - 1\npeople - 1\nwho - 1\nhi - 1\nimproper - 1\n"
                      "spelling - 1\nwhile - 1\nhell0 - 1\nentirely - 1\ndifferent - 1\nword - 1\n12345 - 1\n"
                      "numbers - 1\nspecial - 1\ncharacters - 1\n")
    json_contents = None
    read_file_test_template(capsys, file_name, number_of_words_to_print, return_json, json_name, std_out_string, json_contents)

def test_read_test_file_new_json(capsys):
    json_contents = {"hello": 9, "to": 5, "of": 4, "is": 4, "how": 3, "are": 3, "you": 3, "jimmy": 3, "martha": 3,
                     "say": 3, "myself": 2, "and": 2, "samantha": 2, "want": 2, "an": 2, "a": 2, "sequence": 2, "world": 1,
                     "as": 1, "well": 1, "like": 1, "talking": 1, "together": 1, "saying": 1, "eachother": 1, "wants": 1,
                     "too": 1, "why": 1, "does": 1, "everyone": 1, "list": 1, "people": 1, "who": 1, "hi": 1, "improper": 1,
                     "spelling": 1, "while": 1, "hell0": 1, "entirely": 1, "different": 1, "word": 1, "12345": 1,
                     "numbers": 1, "special": 1, "characters": 1}
    if os.path.exists("test_word_counts.json"):
        os.remove("test_word_counts.json")

    file_name = "test.txt"
    number_of_words_to_print = 10
    return_json = True
    json_name = "word_counts"
    std_out_string = ("hello - 9\nto - 5\nof - 4\nis - 4\nhow - 3\nare - 3\nyou - 3\njimmy - 3\nmartha - 3\nsay - 3\n"
                      "The data was written successfully into the json file: test_word_counts.json\n")
    read_file_test_template(capsys, file_name, number_of_words_to_print, return_json, json_name, std_out_string, json_contents)

def test_read_test_file_existing_json(capsys):
    file_name = "test.txt"
    number_of_words_to_print = 10
    return_json = True
    json_name = "existing_word_counts"
    std_out_string = ("hello - 9\nto - 5\nof - 4\nis - 4\nhow - 3\nare - 3\nyou - 3\njimmy - 3\nmartha - 3\nsay - 3\n"
                      "A file with the name test_existing_word_counts.json already exists; please choose a different name.\n")
    json_contents = None
    read_file_test_template(capsys, file_name, number_of_words_to_print, return_json, json_name, std_out_string, json_contents)