#---------------------< V 3.0.0 >--------------------------
import os
import books_operations as bo
#---------------------< Main >------------------------

while True:
    bo.clear()
    print("---------------------------")
    print("Press A to Add a book")
    print("Press L to List all book")
    print("Press F to Find a book")
    print("Press D to Delete a book")
    print("Press Q to Quit application")
    print("Press S to Save all books")
    print("---------------------------")
    choice = input("Enter your choice: ").upper()
    match choice:
        case "A":
            bo.add_book()
        case "L":
            bo.list_book()
        case "F":
            bo.find_book()
        case "D":
            bo.delete_book()
        case "S":
            bo.save_books()
        case "Q":
            break
        case _:
            print("! ! ! Undefined Choice ! ! !")
            print("---------------------------")
            input("Return?\n")