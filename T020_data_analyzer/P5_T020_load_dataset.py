# Neel Patel T020
# Gabrielle Milburn T020
# Ethan Stewart T020
# Ethan Spooner D'Souza T020

# Book Data Analyzer Version 1.0
# Last Updated: Dec 9, 2021

# Contributions for this file:
# Neel Patel
# Ethan Stewart 

# Imports
import csv

# Function Design
def load_dataset(filename:str) -> dict:
    """Returns a dictionary that sorts a csv by category
    Given file: "Google_Books_Dataset.csv"
    >>>load_dataset("google_book.csv")
    {'Fiction': [{'title': 'The Malady and Other Stories: An Andrzej Sapkowsk...
    """
    book_dictionary = {}
    line_info = []
    newKey = set()
    book_list = []
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for line in csv_reader:
            line_info = []
            line_info.append({"title":line[1],"authors":line[2],"language": line[7],"rating":line[3],"publisher":line[4],"pageCount":line[5]})            
            if (line[1],line[6]) not in book_list:
                if line[6] not in newKey:
                    book_dictionary.update({line[6]:line_info})
                    newKey.add(line[6])
                else:
                    line_info += (book_dictionary.get(line[6]))
                    book_dictionary.update({line[6]:line_info})
            book_list.append((line[1],line[6]))   
    return book_dictionary



