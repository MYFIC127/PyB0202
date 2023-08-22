from json import dumps,loads
from os import system


# collection = []
with open("Codes/books_info.txt","r") as file:
    collection = loads(file.read())

clear = lambda : system("cls")

def print_book(book):
    print("Title: ", book["title"])
    print("Author: ", book["author"])
    print("Pages: ", book["pages"])
    print("Price: ", book["price"])
    print("ISBN: ", book["isbn"])

def add_book():
    clear()
    book = {}
    book["title"] = input("Title: ")
    book["author"] = input("Author: ")
    book["pages"] = int(input("Pages: "))
    book["price"] = float(input("Price: "))
    book["isbn"] = input("ISBN: ")
    collection.append(book)


def list_book():
    clear()
    i = 1
    for book in collection:
        print("---------------------------")
        print(i,".")
        print_book(book)
        i+=1
    print("---------------------------")
    input("Return?\n")

def find_book():
    clear()
    print("---------------------------")
    item_key = input("What is your search basis? (title/author/pages/price/isbn): ")
    wanted_item = input("What is your value? : ")

    if item_key == "pages":                                 #avoids "pages" value erorr
        wanted_item = int(wanted_item)
    elif item_key == "price":                               #avoids "price" value erorr
        wanted_item = float(wanted_item)                    

    i = 0
    for book in collection:
        if book[item_key] ==  wanted_item:
            print("---------------------------")
            print_book(book)
            if item_key == "isbn":
                i = 1 
                break
            else:
                i = 1
    

    if i == 0:
        print("---------------------------")
        print("ERORR 404: No item with such conditions was found")
        print("---------------------------")
        input("Return?\n")

    else:
        print("---------------------------")
        input("Return?\n")

def delete_book():
    clear()
    wanted_item = input("ISBN: ")
    for book in collection:
        if book["isbn"] == wanted_item:
            collection.remove(book)
            break
    else:
        print("---------------------------")
        print("ERORR 404: No item with such conditions was found")    
        print("---------------------------")
        input("Return?\n")

def save_books():
    clear()
    with open("Codes/books_info.txt","w") as file:
        file.write(dumps(collection))
        print("The Database has been updated successfully!")
        input("Return?\n")
