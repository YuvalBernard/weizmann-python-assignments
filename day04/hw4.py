import sys

filename = sys.argv[1]
with open(filename) as f:
    text = f.read().splitlines() # get list of lines

n_lines = len(text)
n_words = sum(len(line.split()) for line in text)
n_characters = sum(len(line) for line in text)

print(f"File '{filename}' contains {n_lines} lines, {n_words} words, and {n_characters} characters.")
