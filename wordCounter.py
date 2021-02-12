# This file contains all functions pertaining to counting words in strings.

import re

# This takes in a string that is the contents of a file with text and
# splits it into a dictionary of individual words with their counts.
# All characters that aren't alphanumerical are removed from the text provided,
# and words are split on spaces, tabs, and line breaks.
# Args:
# file_contents (str) - The string of text from a file to be broken down.
def count_words(file_contents):
    stripped_file_contents = re.sub("[^a-zA-Z0-9 \t\n]+", "", file_contents)
    lowercase_file_contents = stripped_file_contents.lower()
    word_list = list(filter(None, re.split("[ \t\n]+", lowercase_file_contents)))
    word_counts = dict()
    for word in word_list:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts