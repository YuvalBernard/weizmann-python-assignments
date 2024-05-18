import sys
from helper_functions import count_lines, count_words, count_characters

def main():
    filename = sys.argv[1]
    print_file_characteristics(filename)

def print_file_characteristics(filename):
    with open(filename) as file:
        text = file.read().splitlines() # get list of lines
    
    n_lines = count_lines(text)
    n_words = count_words(text)
    n_characters = count_lines(characters)
    print(f"File '{filename}' contains {n_lines} lines, {n_words} words, and {n_characters} characters.")
