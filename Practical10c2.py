# File Indexing using Hashing

index = {
    "data_structure": 1,
    "operating_system": 5,
    "computer_network": 10,
    "python": 15
}

keyword = "python"

if keyword in index:
    print("Keyword:", keyword)
    print("Page Number:", index[keyword])
else:
    print("Keyword not found")