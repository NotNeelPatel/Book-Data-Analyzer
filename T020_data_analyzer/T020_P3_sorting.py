# Ethan Stewart T020
# Ethan Spooner D'Souza T020
# Neel Patel T020
# Gabrielle Milburn T020

# Book Data Analyzer Version 1.0
# Last Updated: Dec 9, 2021

# Contributions for this file:
# to_list, Function 1: Ethan Stewart
# Function 5: Neel Patel
# sort_title_rate_ascending, Functions 2-3: Ethan Spooner D'Souza
# sort_publisher_pageCount, Functions 4-6: Gabrielle Milburn

def to_list(dataset: dict) -> list:
    """Converts the dataset into a list
    >>>to_list(load_dataset("Google_Books_Dataset.csv"))
    [{'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler'...
    """
    book_data = []
    for keys in dataset:
        for items in dataset[keys]:
            book_data.append(items)
    return book_data

def sort_title_rate_ascending(dataset: dict, value: str) -> list:
    """Returns a sorted list by either title or ascending rate
    >>>sort_title_rate_ascending(load_dataset("Google_Books_Dataset.csv"),"title")
    [{'title': 'A Feast for Crows (A Song of Ice and Fire, Book 4)',...
    >>>sort_title_rate_ascending(load_dataset("Google_Books_Dataset.csv"),"rating")
    [{'title': 'No Mercy: The brand new novel from the Queen of Crime',...
    """
    book_data = to_list(dataset)
    for i in range(0, len(book_data)-1):
        for j in range(0, len(book_data)-1-i):
            if ((book_data[j]).get(value) > (book_data[j+1]).get(value)):
                    (book_data[j]), (book_data[j+1]) = (book_data[j+1]), (book_data[j])
    return(book_data)

def sort_publisher_pageCount(book_data: list, value: str) -> list:
    """Returns a sorted list that's already sorted by publisher or pageCount and
    sorts alphabetically when the publisher/pageCount are the same
    >>>sort_publisher_pageCount(to_list(load_dataset("Google_Books_Dataset.csv")),"publisher")
    [{'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler',...
    >>>sort_publisher_pageCount(to_list(load_dataset("Google_Books_Dataset.csv")),"pageCount")
    [{'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler',...
    """
    for i in range(0, len(book_data)-1):
        for j in range(0, len(book_data)-1-i):
            if ((book_data[j]).get(value)) == (book_data[j+1]).get(value) and (book_data[j]).get("title") >= (book_data[j+1]).get("title"):
                (book_data[j]), (book_data[j+1]) = (book_data[j+1]), (book_data[j])
    return book_data

# Function 1
def sort_books_title(dataset: dict) -> list:
    """
    Returns and prints a list of book data in the form of dictionaries,
    the books are sorted by their titles in alphabetical order.
    Given a dictionary where books are stored.
    >>> sort_books_title(book_dictionary)
    [{'title': "'Salem's Lot", 'authors': 'Stephen King', 'language ': 'E ...
    """
    book_data = sort_title_rate_ascending(dataset,"title")
    return book_data

# function 2
def sort_books_ascending_rate(dataset: dict) -> list:
    """
    returns a list of books from book_dictionary sorted in ascending order by rate.
    >>> sort_books_ascending_rate(dataset)
    [{'title': 'No Mercy: The brand new novel from the Queen of Crime', 'authors': 'Martina Cole', 'language ': 'English', 'rating': '', ...
    """
    book_data = sort_title_rate_ascending(dataset,"rating")
    return(book_data)

# function 3
def sort_books_descending_rate(dataset: dict) -> list:
    """
    returns a list of books from book_dictionary sorted in descending order by rate.
    >>> sort_books_descending_rate(dataset)
    [{'title': 'The Red Signal: An Agatha Christie Short Story', 'authors': 'Agatha Christie', 'language ': 'English', 'rating': '5', 'publisher': 'HarperCollins UK', 'pageCount': '40'}, ...
    """
    book_data = to_list(dataset)
    for i in range(0, len(book_data)-1):
        for j in range(0, len(book_data)-1-i):
            if ((book_data[j]).get("rating") < (book_data[j+1]).get("rating")):
                    (book_data[j]), (book_data[j+1]) = (book_data[j+1]), (book_data[j])
    return(book_data)

# Function 4
def sort_books_publisher(dataset:dict):
    """returns  a  list  with  the  book  data  stored  as  a  dictionary  book  where  the  books  are  sorted alphabetically by publisher"""
    book_list = to_list(dataset)
    for i in range(0, len(book_list)):
        for j in range(0, len(book_list)-1-i):
            title_1= book_list[j]
            title_2= book_list[j+1]
            if title_1["publisher"]>title_2["publisher"]:
                book_list[j],book_list[j+1]=book_list[j+1],book_list[j]
    book_list = sort_publisher_pageCount(book_list,"publisher")
    return book_list

# Function 5
def sort_books_pageCount(dataset:dict) -> list:
    """Returns a sorted list of books and their values by page count in ascending order.
    >>>(sort_books_pageCount(book_dictionary))
    [{'title': 'Summary: Think and Grow Rich', 'authors': 'Nine99 Innovation Lab', 'language ': 'English', 'rating': '', 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'pageCount': '14'}...
    """
    book_data = to_list(dataset)
    for i in range(0, len(book_data)-1):
        for j in range(0, len(book_data)-1-i):
            if (int((book_data[j]).get("pageCount")) > int((book_data[j+1]).get("pageCount"))):
                (book_data[j]), (book_data[j+1]) = (book_data[j+1]), (book_data[j])
    book_data = sort_publisher_pageCount(book_data,"pageCount")
    return(book_data)

# Function 6
def sort_books_category(dataset:dict):
    """returns  a  list  with  the  book  data  stored  as  a  dictionary  book  where  the  books  are  sorted alphabetically by category"""
    CategorySort = []
    books = []
    bookCategory = []
    for key in dataset.keys():
            CategorySort += [key] # Assigns the category to the list
    for i in range(len(CategorySort)): # Bubble sort the categories
            for j in range(0, len(CategorySort)-i-1):
                if CategorySort[j] > CategorySort[j+1] :
                    CategorySort[j], CategorySort[j+1] = CategorySort[j+1], CategorySort[j]
    for category in CategorySort:
        bookCategory = []
        for book in dataset.get(category):
            bookCategory += [book]
        for i in range(0, len(bookCategory)-1):
            for j in range(0, len(bookCategory)-1-i):
                if ((bookCategory[j]).get("title")) > (bookCategory[j+1]).get("title"):
                    (bookCategory[j]), (bookCategory[j+1]) = (bookCategory[j+1]), (bookCategory[j])
        books += bookCategory
    return books
