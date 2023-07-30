# Book Data Analyzer V 1.0

By Ethan^2

Book data analyzer is a python program that can extract information from a dataset of books. The program can read a CSV file where book information is stored, and provide the books sorted by category in a dictionary. This dictionary then can be sorted and modified in various ways using the program. 
There are four python files within the book data analyzer, each with a specific purpose. 

**_P5_T020_load_dataset.py_** contains the function that allows the user to load a csv file into the program. 

**_T020_P2_search_modify_dataset.py_** contains the functions that allow for modifications of the dataset, as well as searching specific information within the dataset.

**_T020_P3_sorting.py_** contains the functions that let the dataset be sorted in various ways (category, author, title etc.)

**_T020_data_analyzer.py_** is the user interface that lets the user perform any action possible        from the functions in the previous files. 

## Prerequisites

Ensure Python 3.9 or greater is installed.

One built-in module is used: csv

The csv file being used must follow the following format for the order of attributes:


```
|     | title             | author        | rating | publisher                   | page_count | generes | language |
|-----|-------------------|---------------|--------|-----------------------------|------------|---------|----------|
| 1   | Antiques Roadkill | Barbara Allan | 3.3    | Kensington Publishing Corp. | 288        | Fiction | English  |
| 2   |                   |               |        |                             |            |         |          |
| ... |                   |               |        |                             |            |         |          |
```

## Installation

Download the T020_data_analyzer folder that contains all the project files. 



## Usage
### Setup
Ensure a csv file containing book information is in the same directory as T020_data_analyzer.py, this should be in the T020_data_analyzer folder. 

### Windows/MacOS
In the command prompt (Win) or terminal (Mac), navigate to the folder T020_data_analyzer in which T020_data_analyzer.py is located.
```
cd "folder path"
```
Then to execute the program type:
```
python T020_data_analyzer.py
```
### Linux
In your preferred terminal, navigate to the folder T020_data_analyzer in which T020_data_analyzer.py is located.
```
cd "folder path"
```
Then to execute the program type:
```
python3 T020_data_analyzer.py
```

### Using _T020_data_analyzer.py_

When executed, _T020_data_analyzer.py_ will look like this:

```
1- Command Line L)oad file
2- Command Line A)dd book
3- Command Line R)emove book
4- Command Line F)ind book by title
5- Command Line NC) Number of books in a category
6- Command Line CA) Categories for an author
7- Command Line CB) Categories for a book title
8- Command Line G)et book
       R)ate  A)uthor  P)ublisher  C)ategory
       CT) Category and Title  CR) Category and Rate
9- Command Line S)ort book
       T)itle  R)ate  P)ublisher  C)ategory  PA)ageCount  
10-Command Line Q)uit
```


#### L)oad file
To begin using the program, a file must be loaded (command: _L)oad file_)
```
1- Command Line L)oad file
2- Command Line A)dd book
3- Command Line R)emove book
4- Command Line F)ind book by title
5- Command Line NC) Number of books in a category
6- Command Line CA) Categories for an author
7- Command Line CB) Categories for a book title
8- Command Line G)et book
       R)ate  A)uthor  P)ublisher  C)ategory
       CT) Category and Title  CR) Category and Rate
9- Command Line S)ort book
       T)itle  R)ate  P)ublisher  C)ategory  PA)ageCount  
10-Command Line Q)uit
L

Please Enter a File Name:  
```
Here, the name of the desired csv file can be inputted. (e.g _Google_Books_dataset.csv_)

Once loaded, any action from the list of commands can be completed.

#### A)dd book
Add book is used to add new books into the dataset. 

#### R)emove book
Remove book is used to remove any book from the dataset.

#### F)ind book by title
This command take the input of a book title, and provides the information of that book

#### NC) Number of books in a category
 Take a user input of a category, and returns the number of books within that category

#### CA) Categories for an author
Takes an author from the user, and displays the categories that contain books from that author.

####  CB) Categories for a book title
Takes a book title input form the user, and displays the categories in which that book is held
#### G)et book
This command is split into six sub commands
##### R)ate  
User inputs a rating, and the program returns all of the books with that specified rating. 
##### A)uthor  
User inputs an author, and the program returns all of the books written by that author in the dataset
##### P)ublisher  
User inputs a publisher, and the program returns all of the books published by that publisher 
##### C)ategory
User inputs a category, and the program returns all of the books published in that category
##### CT) Category and Title  
User inputs a book category and title, and the program returns whether there is a book under the inputted category or not
##### CR) Category and Rate
User inputs a book category and rating (from 0 - 5) , and the program returns a list of books titles that have a rating of the inputted rating or greater
#### S)ort book
Like the command above, this is split into four categories:
##### T)itle
The program returns a sorted list of book information sorted by title alphabetically
##### R)ate
The user will be prompted to either input A)scending or D)escending. The program returns a sorted list of book information sorted by rating.
##### P)ublisher
The program returns a sorted list of book information sorted by publishers alphabetically. Books under the same publisher will also be sorted alphabetically within the publishers.
##### C)ategory
The program returns a sorted list of book information sorted by category alphabetically. Books under the same category will also be sorted alphabetically within the category.
##### PA)ge Count
The program returns a sorted list of book information sorted by page count (ascending)

#### Q)uit
This command stops the program.

Once an action is completed, if the command chosen is not Q)uit, the program will display the original commands again, and prompt the user to select another command. All actions will be performed on the dataset currently loaded, until a new dataset is loaded using L)oad file
## Contact

**Neel Patel** (Team Leader)

Email: neelpatel4@cmail.carleton.ca

## Credits/Contributors

Credits of each individual and the functions as well as any elements they worked on:

**Gabrielle Milburn** 
- print_dictionary_category
- add_book
- remove_book
- sort_publisher_pageCount
- sort_books_publisher
- sort_books_category

**Neel Patel**
- load_dataset
- get_books_by_publisher
- check_category_and_title
- all_categories_for_book_title
- sort_books_pageCount
- UI elements

**Ethan Spooner D’Souza**
- get_books_by_rate
- find_books_by_title
- get_books_by_author
- sort_title_rate_ascending
- sort_books_ascending_rate
- sort_books_descending_rate
- UI elements

**Ethan Stewart**
- load_dataset
- get_books_by_category
- get_books_by_category_and_rate
- get_author_categories
- sort_books_title
- to_list

## Project status
**Version 1.0** - 9 Dec 2021

No longer being developed.

## License
[MIT](https://choosealicense.com/licenses/mit/)
