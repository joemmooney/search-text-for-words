# This file is the main file for running this program.

import argparse
from fileReader import read_file

# The main function that is run when starting the program.
# It sets up argument parsing for the file name to read, the number of most common words to print,
# whether to return a json file, and the name for the json file that is being returned.
# Then it sends these arguments to the function that reads and processes the file.
def main():
  parser = argparse.ArgumentParser(description="Arguments being passed to the word count program")
  parser.add_argument("file_name", help="Name of the .txt file to count words in")
  parser.add_argument("--number_of_words_to_print", type=int, default=10, help="The number of words to print " + 
                      "when showing the top n most common words (defaults to 10)")
  parser.add_argument("--return_json", action="store_true", help="If this flag is present, " +
                      "a json file with word counts will be returned")
  parser.add_argument("--json_name", type=str, default="word_counts", help="Part of the name of the json file " +
                      "that the word counts will be saved to (naming convention is \"{file_name}_{json_name}.json\") " + 
                      "(defaults to word_counts)")
  args = parser.parse_args()
  read_file(args.file_name, args.number_of_words_to_print, args.return_json, args.json_name)

if __name__ == "__main__":
  main()