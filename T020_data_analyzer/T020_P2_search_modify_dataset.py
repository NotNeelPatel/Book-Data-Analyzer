# Neel Patel T020
# Gabrielle Milburn T020
# Ethan Stewart T020
# Ethan Spooner D'Souza T020

# Book Data Analyzer Version 1.0
# Last Updated: Dec 9, 2021

# Contributions for this file:
# Functions 1-3: Gabrielle Milburn
# Functions 4-6: Ethan Spooner D'Souza
# Functions 7-9: Neel Patel
# Functions 10-12: Ethan Stewart

# Function 1
def print_dictionary_category(category:str,dictionary:dict)->int:
    """takes the category to print and the dictionary where the data is stored. The function returns the number of elements associated with that key in the dictionary.
    >>>print_dictionary_category('Fiction',book_dictionary)
    The category Fiction  has 39 books. This is the list of books in the category Fiction : [{'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'authors': 'Andrzej Sapkowski'....
    """
    x=dictionary.get(category)
    books=[]
    if x==None:
        print('category not found')
        return 0
    else:
        for list in x:
            books.append(list)
    print("The category",category, " has", len(books), "books. This is the list of books in the category",category,":")
    for x in books:
        print(x)
    return len(books)

# Function 2
def add_book(dictionary:dict,book_info:tuple)->dict:
    """takes two arguments,the dictionary where the book must be added and a tuple argument that has seven values which are title, author, language, publisher, category, rating and pageCount. The function adds the book to the dictionary and verifies that the book has been added.
    >>>b=('book','author','language','rating','Fiction','publisher','pageCount')
    >>>add_book(book_dictionary,b)
    the book has been added correctly
    {'Fiction': [{'title': 'The Malady and Other Stories: An Andrzej Sapkowski...
    """
    category=book_info[4]
    x=dictionary.get(category)
    if x==None:
        print("there was an error adding the book")
        return(dictionary)
    else:
        new_book_info={"title":book_info[0],"authors":book_info[1],"language": book_info[2],"rating":book_info[3],"publisher":book_info[5],"pageCount":book_info[6]}
        dictionary[category].append(new_book_info)
        if new_book_info in x:
            print("the book has been added correctly")
            return(dictionary)
        else:
            print("there was an error adding the book")
            return(dictionary)

# Function 3
def remove_book(title:str,category:str,dictionary:dict)->dict:
    """takes two string arguments, the title of the book and the category, and the dictionary from where the book must be removed . The function returns the updated dictionary with book removed if book is found
    >>>remove_book('The Malady and Other Stories: An Andrzej Sapkowski Sampler','Fiction', book_dictionary)
    the book has been removed correctly
    {'Fiction': [{'title': "Chronicle of the Unhewn Throne: (The Emperor's Blades,...
    """
    updated_cat=[]
    titleFound = False
    x=dictionary.get(category)
    if x==None:
        print ("Error removing book. Category not found")
        return(dictionary)
    for titles in x:
        for i in x:
            if i.get('title') == title:
                titleFound = True
            else:
                updated_cat.append(i)
        if not titleFound:
            print ("Error removing book. Title not found")
            return(dictionary)
        dictionary[category]=(updated_cat)
        print("the book has been removed correctly")
        return(dictionary)

# Function 4
def get_books_by_rate(rate: int, book_dict: dict) -> dict:
    """
    returns a dictionaty with all the books that have the specified rate.
    >>> get_books_by_rate(3, load_dataset('google_book.csv'))
    {'Mrs. Pollifax Unveiled': ['Title: Mrs. Pollifax Unveiled', 'Authors: Dorothy Gilman', 'Language: English', 'Rating: 3.9', 'Publisher: Ballantine Books', 'Category: Fiction', 'Page Count: 208'],
    """
    try:
        keys = []
        for i in book_dict:  # get all the keys
            keys.append(i)
        booktitles = {}  # list of all book titles we want
        rate = int(rate)
        for i in keys:  # get all the of the individual books
            for j in (book_dict[i]):
                if (j["rating"]) != "":  # make sure there is no "" str -> float
                    if rate <= (float(j["rating"])) < (rate+1):
                        if j["title"] not in booktitles:
                            booktitles[(j.get("title"))] = ["Title: " + j.get("title"),"Authors: "+ (j["authors"]),"Language: "+ (j["language"]),"Rating "+ str(j["rating"]),"Publisher: "+ (j["publisher"]),"Category: " + i,"Page Count: " + str(j["pageCount"])]
        for i in booktitles:
            print("\n")
            for j in booktitles[i]:
                print(j)
    except:
        print("Error: Rate not int value")
    return (booktitles)

# Function 5
def find_books_by_title(title: str, book_dict: dict) -> bool:
    """
    returns True or False depending on if book (title) is present
    within the specified genre (the key of the the dictionaty)
    >>> find_books_by_title("Antiques Knock-Off", load_dataset('google_book.csv'))
    True
    """
    ret = False
    for genre in book_dict:
        for i in (book_dict[genre]):
            if (i["title"]) == title:
                ret = True
    if ret == True:
        print("The book has been found")
    else:
        print("The book has NOT been found")
    return(ret)

# Function 6
def get_books_by_author(author: str, book_dict: dict) -> list:
    """
    returns a list containing the titles of books of a given author within the
    specified genre.
    >>> get_books_by_author("Agatha Christie", load_dataset('google_book.csv'))
    ['The Mysterious Affair at Styles', 'And Then There Were None', 'The Red Signal: An Agatha Christie Short Story']
    """
    titlelist = []
    for genre in book_dict:
        for i in (book_dict[genre]):
            if (i['authors']) == author and (i['title']) not in titlelist:
                titlelist += [i.get('title')]
    print("The author “" + str(author) + "” has published the following books:")
    x = 1
    for i in titlelist:
        print("    "+str(x)+"- "+i)
        x += 1
    return(titlelist)

#Function 7
def get_books_by_publisher(publisher:str, book_dictionary:dict) -> list:
    """Returns a list of book titles of a specified publisher
    >>>get_books_by_publisher("AMACOM",book_dictionary)
    The publisher "AMACOM", has published the following books:
    1- Marketing (The Brian Tracy Success Library)
    2- The Essentials of Finance and Accounting for Nonfinancial Managers
    3- Personal Success (The Brian Tracy Success Library)
    4- Management (The Brian Tracy Success Library)
    5- Business Strategy (The Brian Tracy Success Library)
    ['Marketing (The Brian Tracy Success Library)', 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'Personal Success (The Brian Tracy Success Library)', 'Management (The Brian Tracy Success Library)', 'Business Strategy (The Brian Tracy Success Library)']
    """
    book_publisher_list = []
    for key in book_dictionary.keys():
        list_values = book_dictionary.get(key)
        list_num = 0
        for item in list_values:
            if publisher == item.get('publisher'):
                if not list_values[list_num].get('title') in book_publisher_list:
                    book_publisher_list.append(list_values[list_num].get('title'))
            list_num += 1
    print("The publisher \""+publisher+"\", has published the following books:")
    for i in range(len(book_publisher_list)):
        print(str(i+1)+"-",book_publisher_list[i])
    return book_publisher_list

# Function 8
def check_category_and_title(category:str, title:str, book_dictionary:dict) -> bool:
    """Returns True if the title exists under the specified category, and returns false if it doesn't
    >>>check_category_and_title("Fiction","After Anna",book_dictionary)
    The category Fiction has the book title After Anna
    True
    >>>check_category_and_title("Comics","Black Panther",book_dictionary)
    The category Comics does not have the book title Black Panther
    False
    """
    if category in book_dictionary.keys():
        list_values = book_dictionary.get(category)
        for item in list_values:
            if title == item.get('title'):
                print("The category",category,"has the book title",title)
                return True
        print("The category",category,"does not have the book title",title)
        return False
    print("The category",category,"does not exist")
    return False

# Function 9
def all_categories_for_book_title(title:str, book_dictionary:dict):
    """Returns a list of genres under of a specified book title
    >>>all_categories_for_book_title("Sword of Destiny: Witcher 2: Tales of the Witcher", book_dictionary)
    The book title "Sword of Destiny: Witcher 2: Tales of the Witcher", has published the following categories:
    1- Fiction
    2- Adventure
    3- Mythical Creatures
    ['Fiction', 'Adventure', 'Mythical Creatures']
    """
    book_category_list = []
    for key in book_dictionary.keys():
        list_values = book_dictionary.get(key)
        list_num = 0
        for item in list_values:
            check_publisher =  item.get('title')
            if title == item.get('title'):
                book_category_list += [key]
            list_num += 1
    print("The book title \""+title+"\", is in the following categories:")
    for i in range(len(book_category_list)):
        print(str(i+1)+"-",book_category_list[i])
    return book_category_list

# Function 10
def get_books_by_category(category: str, book_dictionary: dict) -> list:
    """
    Returns a list of the books titles for the given category.
    >>> get_books_by_category('Adventure', book_dictionary)
    The category "Adventure" has the following books:

       1- The Malady and Other Stories: An Andrzej Sapkowski Sampler
       2- Edgedancer: From the Stormlight Archive
       3- A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
       4- The Way Of Shadows: Book 1 of the Night Angel
       5- After Anna
       6- A Feast for Crows (A Song of Ice and Fire, Book 4)
       7- Sword of Destiny: Witcher 2: Tales of the Witcher
    ['The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'Edgedancer: From the Stormlight Archive', 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'The Way Of Shadows: Book 1 of the Night Angel', 'After Anna', 'A Feast for Crows (A Song of Ice and Fire, Book 4)', 'Sword of Destiny: Witcher 2: Tales of the Witcher']
    """
    list_titles = []
    count = 1
    print('The category', '"'+category+'"', 'has the following books:\n')
    if category in book_dictionary.keys():
        for dictionary in book_dictionary.get(category):
            list_titles.append(dictionary.get('title'))
            print('  ',str(count)+"-", str(dictionary['title']))
            count += 1
        return list_titles

# Function 11
def get_books_by_category_and_rate(category: str, rate: int, book_dictionary: dict) -> list:
    """
    Returns a list of book titles for the given category and rate interval.
    >>> get_books_by_category_and_rate('Adventure', 4, book_dictionary)
    The category "Adventure" and rate 4 has the following books:

       1- The Malady and Other Stories: An Andrzej Sapkowski Sampler
       2- Edgedancer: From the Stormlight Archive
       3- A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
       4- The Way Of Shadows: Book 1 of the Night Angel
       5- After Anna
       6- A Feast for Crows (A Song of Ice and Fire, Book 4)
       7- Sword of Destiny: Witcher 2: Tales of the Witcher
    ['The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'Edgedancer: From the Stormlight Archive', 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'The Way Of Shadows: Book 1 of the Night Angel', 'After Anna', 'A Feast for Crows (A Song of Ice and Fire, Book 4)', 'Sword of Destiny: Witcher 2: Tales of the Witcher']
    """
    list_titles = []
    count = 1
    print('The category', '"'+category+'"', 'and rate', rate, 'has the following books:')
    print()
    try:
        rate = int(rate)
        if category in book_dictionary.keys():
            for dictionary in book_dictionary[category]:
                if dictionary.get('rating') != '' and rate <= float(dictionary.get('rating')) < rate + 1:
                    list_titles.append(dictionary.get('title'))
                    print('  ',str(count)+"-", str(dictionary['title']))
                    count += 1        
    except:
        print("Error: Rate not int value")
    return list_titles

# Function 12
def get_author_categories(author: str, book_dictionary: dict) -> list:
    """
    Returns a list of categories for the given author.
    >>> get_author_categories('Blake Pierce', book_dictionary)
    The author "Blake Pierce" has published books under the following categories:

       1- Fiction
       2- Detective
       3- Thrillers
       4- Mystery
    ['Fiction', 'Detective', 'Thrillers', 'Mystery']
    """
    list_categories = []
    count = 1
    print('The author', '"'+author+'"', 'has published books under the following categories:')
    print()
    for keys in book_dictionary.keys():
        #print(keys)
        for books in book_dictionary.get(keys):
            #print(books)
            if books.get('authors') == author and keys not in list_categories:
                #print(1)
                list_categories.append(keys)
                print('  ',str(count)+"-", str(keys))
                count += 1
    return list_categories
