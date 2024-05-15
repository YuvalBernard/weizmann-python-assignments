import sys
def main():
    filename = sys.argv[1]
    print_file_characteristics(filename)

def print_file_characteristics(filename):
    with open(filename) as file:
        text = file.read().splitlines() # get list of lines
    
    n_lines = len(text)
    n_words = sum(len(line.split()) for line in text)
    n_characters = sum(len(line) for line in text)
    print(f"File '{filename}' contains {n_lines} lines, {n_words} words, and {n_characters} characters.")
