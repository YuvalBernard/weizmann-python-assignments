ncbi.py downloads user requested terms from the NCBI database and keeps track of the search history.

Required packages: `Bio, datetime`.

Defined functions:
- `search_ncbi(term, number)`: searches NCBI for`term` and `number` and returns the search record.
- `download_from_ncbi(term, number)`: downloads the data and saves it to a file in the "downloads" directory.
   It also saves the search history in a file called "search_history.csv".
