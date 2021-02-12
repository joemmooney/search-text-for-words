# This file contains all functions pertaining to handling json files.

import json

# Takes in a dictionary and writes it to a json file titled file_name.
# This program prints an error message if a file with that name already exists.
# Args:
# dictionary (dict{str: t}) - The dictionary of items to write into a json file.
# file_name (str) - The name of the json file to create.
def create_json(dictionary, file_name):
    try:
        json_file = open(file_name, "x")
        json.dump(dictionary, json_file)
        print("The data was written successfully into the json file: " + file_name)
    except FileExistsError:
        print("A file with the name " + file_name + " already exists; please choose a different name.")
    except:
        print("There was an issue writing the data to the json file.")