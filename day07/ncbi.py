import os
import sys
import csv
from datetime import datetime
from Bio import Entrez

Entrez.email = "yuval.bernard@weizmann.ac.il"

def search_ncbi(term, number):
    handle = Entrez.esearch(db='protein', term=term, idtype="acc", retmax=number)
    record = Entrez.read(handle)
    return record["Count"], record["IdList"]


def download_from_ncbi(term, number):
    Count, IdList = search_ncbi(term, number)    
    os.makedirs("downloads", exist_ok=True)
    filenames = [f"{term}_{id}.gb" for id in IdList]

    for filename, search_id in zip(filenames, IdList):
        print(f"Fetching data into {filename}...")
        data = Entrez.efetch(db="protein", id=search_id, rettype="gb", retmode="text").read()
        with open(os.path.join("downloads", filename)) as f:
            f.write(data)

    with open("search_history.csv", "a", newline="") as file:
        fields = ["date", "term", "max", "total"]
        writer = csv.DictWriter(file, fieldnames=fields)
        if not os.path.isfile("search_history.csv"):
            writer.writeheader()
        writer.writerow({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "term": term,
            "max": len(IdList),
            "total": Count
        })

def main():
    if len(sys.argv) != 3:
        exit(f"Insert term and number to search.")
    term = sys.argv[1]
    count = int(sys.argv[2])
    download_from_ncbi(term, count)

if __name__ == "__main__":
    main()
