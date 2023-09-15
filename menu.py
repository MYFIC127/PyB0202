#-----------< The Final Project for the PyB0202 course >--------------
#-------------------------< V 3.3.3 >---------------------------------
#-------------------------< M.Y.Fozi >--------------------------------
#TODO:1.menu 2.add functions 3.debug 4.welcome page(maybe) 5.finishing touches
#FIXME:
#-------------------------< Imports >-------------------------------
import student_operations as so
#-----------------------------< Main >--------------------------------
so.clear()
print("---------------------------------------------------------------------------")
print("\t\t\t\tWelcoome")
print("\t\tTurn up your volume for the best experince!")
print("---------------------------------------------------------------------------")
so.startup_jingle()
input("Press any key ...")
while True:
    so.clear()
    print("---------------------------------------------------------------------------")
    print("Please choose your desired action by entering one of the following letters:")
    print()
    print("'N' to Add a new entry")
    print("'F' to Search between the entries")
    print("'R' to Remove an entry")
    print("'C' to Change a course")
    print("'L' to List all enteries")
    print("'U' to Update the database")
    # print("'P' to Open the app preferences")    #autosave/jingles/welcome screen/list view toggles
    print("'Q' to Exit the applicaton")
    print("---------------------------------------------------------------------------")
    choice = input("Please enter a valid option: ").upper()
    # maybe a cool waiting for input animation

    match choice:
        case "N":
            so.new_entry()
        case "L":
            so.list_entries()
        case "F":
            so.find_entry()
        case "R":
            so.remove_entry()
        case "C":
            so.change_course()
        case "U":
            so.update()
        # case "P": 
        case "Q":
            if input("! Are you sure? Any unsaved changes will be lost! ('yes'): ") == "yes":
                so.quit_jingle()
                break
        case _:
            print("! ! ! Undefined Choice ! ! !")
            print("---------------------------------------------------------------------------")
            so.fail_jingle()
            input("Return?\n")