import sys

filename = sys.argv[1]
with open(filename) as f:
    text = f.read().splitlines() # get list of lines

lines = len(text)
words = sum(len(line.split()) for line in text)
characters = sum(len(line) for line in text)

print(f"File '{filename}' contains {lines} lines, {words} words, and {characters} characters.")
