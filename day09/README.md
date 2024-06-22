# Analyze DNA Sequence

This script recieves a path to a dna sequence in Fasta or GenBank format,
and lets the user either:
* find the longest repeating sequence
* locate transcription factor binding sites (TFBS), represented by the sequence TCAGGTCA.

### Dependencies
Install via pip using `requirements.txt`.
```
pip install -r requirements.txt
```

### Usage
```
python analyze_dna_sequence.py --path=PATH [--duplicate] [--tfbs]
```
* Specify path to sequence via `--path=PATH` (required)
* Find longest repeating sequence by specifying `--duplicate` (optional)
* Locate TFBS by specifying `--tfbs` (optional)
