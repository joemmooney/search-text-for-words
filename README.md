Application to count words in a .txt file.

Run locally by doing the following:

1) Download project from GitHub.
2) Enter terminal.
3) Navigate to project folder.
4) Run 'pipenv shell' in terminal to enter the pipenv shell (requires pipenv downloaded on computer).
5) Run 'pipenv install -r requirements.txt' to install all dependencies (only needed first time).
6) Put the text file you want to read in the folder with the program.
7) Run 'python setup.py {file_name}' to run program.

You can view information about the arguments for the program by running 'python setup.py -h'.

Runtime args:
setup.py [-h] [--number_of_words_to_print INT] [--return_json] [--json_name STR] file_name
 -h, --help: Show help message for program.
 --number_of_words_to_print INT: The number of words to print when showing the top n most common words (defaults to 10).
 --return_json: If this flag is present, a json file with word counts will be returned.
 --json_name STR: Part of the name of the json file that the word counts will be saved to (naming convention is "{file_name}_{json_name}.json") (defaults to word_counts).
 
 You can run the automated tests for the program by running 'pytest' in the terminal.
 You can view more verbose details on the test by adding the '-v' or '-vv' flag to the pytest command.
 You can run tests in parallel batches of size INT by adding the '-n INT' argument to the pytest command.
 
 This program is made in python version 3.9.
