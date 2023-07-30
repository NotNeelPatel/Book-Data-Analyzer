# Neel Patel T020
# Gabrielle Milburn T020
# Ethan Stewart T020
# Ethan Spooner D'Souza T020

# Book Data Analyzer Version 1.0
# Last Updated: Dec 9, 2021

# Contributions for the UI:
# Ethan Spooner D'Souza
# Neel Patel

# Contributions for the Cases:
# Case 1: Gabrielle Milburn
# Case 2: Neel Patel 
# Case 3: Ethan Stewart
# Case 4: Ethan Spooner D'Souza

# Imports
from P5_T020_load_dataset import load_dataset
from T020_P2_search_modify_dataset import add_book, remove_book, find_books_by_title, print_dictionary_category, find_books_by_title, all_categories_for_book_title, get_author_categories, get_books_by_rate, get_books_by_author, get_books_by_publisher, check_category_and_title, get_books_by_category_and_rate, get_books_by_category
from T020_P3_sorting import sort_books_title, sort_books_ascending_rate, sort_books_descending_rate, sort_books_publisher, sort_books_pageCount, sort_books_category
    
file = ""
valid_commands = ["L","A","R","F","NC","CA","CB","G","S"]
        
# Function Definition
while True:
    print("\n1- Command Line L)oad file\n2- Command Line A)dd book\n3- Command Line R)emove book\n4- Command Line F)ind book by title\n5- Command Line NC) Number of books in a category\n6- Command Line CA) Categories for an author\n7- Command Line CB) Categories for a book title\n8- Command Line G)et book\n\tR)ate  A)uthor  P)ublisher  C)ategory\n\tCT) Category and Title  CR) Category and Rate\n9- Command Line S)ort book\n\tT)itle  R)ate  P)ublisher  C)ategory  PA)ageCount \n10-Command Line Q)uit")
    command = input("\n: ").upper()
    if command == "Q":
        exit()
    elif (file == "" and command in valid_commands) or (command == 'L'):
        try:
            file = load_dataset(input("Please Enter a File Name: "))
        except FileNotFoundError:
            file = ""
            command = "invalid"
            print("Error: File not found, please try again\n")
            
    if (command in valid_commands):
        # Case 1
        if command=='A':
            try:
                title = (input("Enter book title: "))
                author = input("Enter author name: ")
                lan = input("Enter language: ")
                rate = str(int(input("Enter rating: ")))
                category = input("Enter category: ")
                pub = input("Enter publisher: ")
                pagecount = str(int(input("Enter page count: ")))
                book_tuple = (title, author, lan, rate, category, pub, pagecount)
                file = (add_book((file),book_tuple))                
            except:
                print("\nError: Invalid input\n")
            
        elif command=='R':
            category=(input("Please provide the book category:"))
            file = (remove_book(input("please provide title:"),category,(file)))
        elif command=='F':
            (find_books_by_title(input("please provide title:"),(file)))   
            
        # Case 2
        elif command == "NC":
            print_dictionary_category(input("Please input a category: "), file)        
        elif command == "CA":
            get_author_categories(input("Please input an author: "), file)
        elif command == "CB":      
            all_categories_for_book_title(input("Please input a book title: "), file)
            
        # Case 3
        elif command == 'G':
            print("\nR)ate", "\nA)uthor", "\nP)ublisher", "\nC)ategory", "\nCT) Category and Title", "\nCR) Category and Rate", "\n")
            command = input(": ").upper()
            if command == 'R':
                get_books_by_rate((input("Enter rate: ")), file)
            elif command == 'A':
                get_books_by_author(input("Enter author: "), file)
            elif command == 'P':
                get_books_by_publisher(input("Enter publisher: "), file)
            elif command == 'C':
                get_books_by_category(input("Enter category: "), file)
            elif command == 'CT':
                check_category_and_title(input("Enter category: "), input("Enter title: "), file)         
            elif command == 'CR':
                get_books_by_category_and_rate(input("Enter category: "), (input("Enter rate: ")), file)
            else:
                print("Error: Invalid input") 
                
        # Case 4
        elif command == 'S':
            print("\nT)itle\nR)ate\nP)ublisher\nC)ategory\nPA)ageCount")
            command = input("\n: ").upper()
            if command == 'T':
                print(sort_books_title(file))
            elif command == 'R':
                print("in what order would you like it to be sorted?")
                direction = input("ascending(A) or descending(D): ").upper()
                if direction == 'A':
                    print(sort_books_ascending_rate(file))
                elif direction == 'D':
                    print(sort_books_descending_rate(file))
                else:
                    print("invalid input, please try again")
            elif command == 'P':
                print(sort_books_publisher(file))
            elif command == 'C':
                print(sort_books_category(file))
            elif command == 'PA':
                print(sort_books_pageCount(file))  
            else:
                print("Error: Invalid input")            
    else:
        print("Error: Invalid input")
