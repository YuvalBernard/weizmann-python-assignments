import argparse
import re 
from Bio import SeqIO
from pandas import DataFrame

def open_file(path, file_type):
    sequence = ""
    for seq_record in SeqIO.parse(path, file_type):
        sequence = str(seq_record.seq)
    return sequence

def longest_duplicate(sequence):
    length = 1
    result = ""
    while True:
        regex = r"([GATC]{" + str(length) + r"}).*\1"
        match = re.search(regex, sequence)
        if match:
            result = match.group(1)
            length += 1
        else:
            break
    return result, len(result)

def find_TFBS(sequence):
    # Find Finding Transcription Factor Binding Sites (TFBSs)
    pattern = "TCAGGTCA"
    matches = re.finditer(pattern, sequence)
    return [(match.start(), match.end()) for match in matches]

def main():
    parser = argparse.ArgumentParser(description= "analyze DNA sequences to find duplications and Transcription Factor Binding Sites (TFBSs)")
    parser.add_argument('--path', help="path to fasta/GeneBank file", required=True)
    parser.add_argument('--duplicate', action= "store_true", help= "Find the longest repeating subsequence and its length")
    parser.add_argument('--tfbs', action= "store_true", help= "Find location of Transcription Factor Binding Sites")
    args = parser.parse_args()

    if not args.duplicate and not args.tfbs:
        parser.error('No action requested, add --duplicate or --tfbs')

    path = args.path
    file_type = 'fasta' if path.endswith('.fasta') or path.endswith('.fa') else 'genbank'
    sequence = open_file(path, file_type)

    if args.duplicate:
        duplicate_sequence, duplicate_length = longest_duplicate(sequence)
        print(f'The longest duplicated sequence is: {duplicate_sequence} and its length is: {duplicate_length}\n')

    if args.tfbs:
        locations = find_TFBS(sequence)
        print(f"Transcription Factor Binding Sites were found at locations:\n{DataFrame(find_TFBS(sequence), columns=['Start', 'End'])}")


if __name__ == "__main__":
    main()
