# This file contains all functions pertaining to reading a txt file with a set of arguments
# and setting up the correct actions to take when analyzing that file.

from wordCounter import count_words
from jsonHandler import create_json

# Takes in a file name with a set of arguments and counts the words in that file.
# Then the most common of these words will be printed, and the whole set of them may
# be sent to a new json file.
# Args:
# file_name (str) - Name of the .txt file to count words in.
# number_of_words_to_print (int) - The number of words to print when showing the top n most common words.
# return_json (bool) - Whether a json file with word counts will be returned.
# json_name (string) - Part of the name of the json file (naming convention is "{file_name}_{json_name}.json").
def read_file(file_name, number_of_words_to_print, return_json, json_name):
    try:
        file = open(file_name, "r")
        file_contents = file.read()
    except:
        print("An error was ecountered trying to open the file you specified.")
        return
    word_counts = count_words(file_contents)
    print_top_words(word_counts, number_of_words_to_print)
    if return_json:
        json_file_name = file_name.replace(".txt", "") + "_" + json_name + ".json"
        create_json(word_counts, json_file_name)

# Takes in a dictionary containing all of the words in the file with their counts,
# and then prints the top n most common words based on the number of words argument.
# Args:
# word_counts (dict{str: int}) - Each word in the file and the count of the number of times it appears.
# number_of_words_to_print (int) - The number of words to print.
def print_top_words(word_counts, number_of_words_to_print):
    words = list(word_counts.keys())
    counts = list(word_counts.values())
    for _ in range(number_of_words_to_print):
        if len(words) < 1:
            return
        top_index = counts.index(max(counts))
        print(words.pop(top_index) + " - " + str(counts.pop(top_index)))