#-----------< The Final Project for the PyB0202 course >--------------
#-------------------------< V 3.3.3 >---------------------------------
#-------------------------< M.Y.Fozi >--------------------------------
#TODO:
#FIXME: 
#-----------------------< Imports >-----------------------------
from os import system
from datetime import datetime as dt
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from json import dumps,loads
from winsound import Beep#,PlaySound
# from time import sleep,time
# from threading import Thread
# from sys import stdout
#-----------------------< Errors >-----------------------------
class IsNotUnique(Exception):
    pass
class IsNotDate(Exception):
    pass
class IsNotMeli(Exception):
    pass
class IsNotCode(Exception):
    pass
#-----------------------< Base Functions >-----------------------------
clear = lambda : system("cls")

try:                                                            #Loaders
    with open("active_students.txt","r") as file:
        active_students = loads(file.read())
except(FileNotFoundError):
    active_students = []

try:
    with open("graduated_students.txt","r") as file:
        graduated_students = loads(file.read())
except(FileNotFoundError):
    graduated_students = []



def update():                                                      #save
    clear()
    with open("active_students.txt","w") as file:
        file.write(dumps(active_students))
    with open("graduated_students.txt", "w") as file:
        file.write(dumps(graduated_students))
    print("---------------------------------------------------------------------------")
    print("The Database has been updated successfully!")
    print("---------------------------------------------------------------------------")
    success_jingle()
    input("Press any key ...")



def print_entry(student):                                       #print
    print(f"\tFirst Name: {student['first_name']}")
    print(f"\tLast Name: {student['last_name']}")
    now = dt.now()
    bday = student['birthday']
    bday_p = parse(bday)
    bday_pstr = str(bday_p).strip(" 00:00:00")
    difference = relativedelta(now, bday_p)
    print(f"\tBirthday: {bday_pstr}")
    print(f"\tAge: {difference.years}")
    print(f"\tCode Meli: {student['code_meli']}")
    print(f"\tStudent Code: {student['student_code']}")
    grades_list = student["grades"]
    maxg = max(grades_list)
    ming = min(grades_list)
    avg = round(sum(grades_list) / len(grades_list),2)
    print(f"\tTheir Highest Grade: {maxg}")
    print(f"\tTheir Lowest Grade: {ming}")
    print(f"\tThe Average of Their Grades: {avg}")
    i = 0
    for course in student["courses"]:
        grade = student["grades"][i]
        print(f"\t\t|{i+1}.Course's Name: {course}\tCourse's Grade: {grade}")
        i += 1



def check_meli(meli):                                   #Validators
    if len(str(meli)) == 10:
        for student in active_students:
            if student["code_meli"] == meli:
                raise IsNotUnique
    else:
        raise IsNotMeli

def check_code(code):
    if len(str(code)) == 5:
        for student in active_students:
            if student["student_code"] == code:
                raise IsNotUnique
    else:
        raise IsNotCode
#-----------------------< Operation Functions >-----------------------------
def new_entry():                                      #Add
    clear()
    student = {}
    courses = []
    grades =  []
    more_courses = 0
    i = 1
    print("---------------------------------------------------------------------------")
    print("Please enter the following details")
    student["first_name"] = input("First Name: ")
    student["last_name"] = input("Last Name: ")
    while True:
        try:
            student["birthday"] = input("Birthday (Gregorian)(yyyy/mm/dd): ")   
            bday = student['birthday']                  #I'm saving as string here for saving purposes, but I cast it into a date format everytime it's needed
            bday_p = parse(bday)
            break
        except :
            print("!<ERROR> The Date format is wrong!")
            fail_jingle() 
    while True:
        try:
            meli = input("Code Meli: ")        
            check_meli(meli)
            student["code_meli"] = meli
            break
        except IsNotMeli:
            print("!<ERROR> The Meli Code can ONLY be 10 digit long!")
            fail_jingle()     
        except IsNotUnique:
            print("!<ERROR> The Code MUST be UNIQUE!")
            fail_jingle()
        # except ValueError:                                    #using int is problematic eg:(00256481) turns to (25668481)
        #     print("!<ERROR> The Value must be a NUMBER!")
        #     fail_jingle()

    while True:
        try:
            code = input("Student Code: ")      
            check_code(code)
            student["student_code"] = code
            break
        except IsNotCode:
            print("!<ERROR> The Student Code can ONLY be 5 digit long!")
            fail_jingle()
        except IsNotUnique:
            print("!<ERROR> The Code MUST be UNIQUE!")
            fail_jingle()
        # except ValueError:                                      #using int is problematic eg:(00256481) turns to (25668481)
        #     print("!<ERROR> The Value must be a NUMBER!")
        #     fail_jingle()

    while more_courses == 0:
        courses.append(input(f"{i}. Course name: "))
        while True:
            try:
                grades.append(int(input(f"{i}. Course Grade: ")))
                break
            except ValueError:
                print("!<ERROR> The Value must be a NUMBER!")
                fail_jingle()
        i+=1
        if input("Do you want to add more courses? ('no'/any other key='yes'): ") == "no":
            more_courses = 1
    student["courses"] = courses
    student["grades"] = grades
    active_students.append(student)
    clear()
    print("---------------------------------------------------------------------------")
    print_entry(student)
    print("---------------------------------------------------------------------------")
    print("This entry has been registered successfully!")
    print("---------------------------------------------------------------------------")
    success_jingle()
    input("Press any key ...")



def find_entry():                                                           #find
    clear()
    print("---------------------------------------------------------------------------")
    scode = input("Enter the Student Code: ")
    for student in active_students:
        if student["student_code"] == scode:
            print("---------------------------------------------------------------------------")
            print_entry(student)
            print("---------------------------------------------------------------------------")
            success_jingle()
            break
    else:
        for student in graduated_students:
            if student["student_code"] == scode:
                print("---------------------------------------------------------------------------")
                print_entry(student)
                print("---------------------------------------------------------------------------")
                success_jingle()
                break
        else:
            print("The wanted student does not exist in the database!")
            fail_jingle()
    input("Press any key ...")



def remove_entry():                                                            #remove
    clear()
    print("---------------------------------------------------------------------------")
    scode = input("Enter the Student Code: ")
    for student in active_students:
        if student["student_code"] == scode:
            print("---------------------------------------------------------------------------")
            print_entry(student)
            print("---------------------------------------------------------------------------")
            print("What do you wish to do with this entry?:")
            print("'D' to PERMENANTLY delete the entry")
            print("'M' to Move this entry to the Graduated Students category")
            print("'G' to Return to the Main Menu")
            print("---------------------------------------------------------------------------")
            choice = input("PLease enter a valid option: ").upper()

            match choice:
                case "D":
                    print("---------------------------------------------------------------------------")
                    print("Successful!")
                    print("---------------------------------------------------------------------------")
                    active_students.remove(student)
                    success_jingle()
                case "M":
                    print("---------------------------------------------------------------------------")
                    print("Successful!")
                    print("---------------------------------------------------------------------------")
                    graduated_students.append(student)
                    active_students.remove(student)
                    success_jingle()
                case "G":
                    break
                case _:
                    print("! ! ! Undefined Choice ! ! !")
                    print("---------------------------------------------------------------------------")
                    fail_jingle()
                    input("Press any key ...")
            break
    else:
        print("The wanted student does not exist in the database!")
        fail_jingle()
        
    input("Press any key ...")



def change_course():                                            #change
    clear()
    print("---------------------------------------------------------------------------")
    scode = input("Enter the Student Code: ")
    for student in active_students:
        if student["student_code"] == scode:
            print("---------------------------------------------------------------------------")
            print_entry(student)
            courses = student["courses"]
            grades = student["grades"]
            print("---------------------------------------------------------------------------")
            print("Which of the following operations would you like to perform?")
            print("'A' to Add a course")
            print("'C' to Change a course's details")
            print("'D' to delete a course")
            print("---------------------------------------------------------------------------")
            decicion = input("Please enter a valid option: ").upper()
            match decicion:
                case "A":
                    courses.append(input(f"New Course's name: "))
                    while True:
                        try:
                            grades.append(int(input(f"New Course's Grade: ")))
                            break
                        except ValueError:
                            print("!<ERROR> The Value must be a NUMBER!")
                            fail_jingle()
                    student["courses"] = courses
                    student["grades"] = grades

                case "D":
                    choice = int(input("Which course's information do you wish to alter? : ")) - 1
                    course = student["courses"][choice]
                    grade = student["grades"][choice]
                    print("---------------------------------------------------------------------------")
                    print(f'The course selected for PERMENANT DELETION is: "{course}", with a grade of: "{grade}".')
                    if input('Are you sure? ("yes"): ') == "yes":
                        del courses[choice]
                        del grades[choice]

                case "C":
                    choice = int(input("Which course's information do you wish to alter? : ")) - 1
                    course = student["courses"][choice]
                    grade = student["grades"][choice]
                    print("---------------------------------------------------------------------------")
                    new_course = input(f'The curent value is "{course}". What do you want to change this into: ')
                    student["courses"][choice] = new_course
                    while True:
                        try:
                            new_grade = int(input(f'The curent value is "{grade}". What do you want to change this into: '))
                            student["grades"][choice] = int(new_grade)
                            break
                        except ValueError:
                            print("!<ERROR> The Value must be a NUMBER!")
                            fail_jingle()

                case _:
                    print("! ! ! Undefined Choice ! ! !")
                    print("---------------------------------------------------------------------------")
                    fail_jingle()
                    input("Press any key ...")


            clear()
            print("---------------------------------------------------------------------------")
            print("The operation has been successful. Here's the new profile: ")
            print("---------------------------------------------------------------------------")
            print_entry(student)
            print("---------------------------------------------------------------------------")
            success_jingle()
            break
            
    else:
        print("The wanted student does not exist in the database!")
        fail_jingle()
    input("Press any key ...")



def list_entries():                                             #list
    clear()
    choice = input("Which veiw do you want('C' = compact/'D' = detailed): ").upper()
    match choice:
        case "D":
            clear()
            print("---------------------------------------------------------------------------")
            print("\n\t\t\t    Active Students:\n")
            
            for student in active_students :
                print("---------------------------------------------------------------------------")
                print_entry(student)
            print("---------------------------------------------------------------------------")
            print("\n\t\t\t    Graduated Students:\n")
            for student in graduated_students :
                print("---------------------------------------------------------------------------")
                print_entry(student)
            print("---------------------------------------------------------------------------")
            success_jingle()
            input("Press any key ...")
        case "C":
            clear()
            i = 1
            print("---------------------------------------------------------------------------")
            print("row \tfirst name     last name      Meli Code      Student Code")
            print("---------------------------------------------------------------------------")
            for student in active_students:
                print(f"{i})\t{student['first_name']:15}{student['last_name']:15}{student['code_meli']:15}{student['student_code']:15}")
                i += 1
            i = 1
            print("---------------------------------------------------------------------------")
            for student in graduated_students:
                print(f"{i})\t{student['first_name']:15}{student['last_name']:15}{student['code_meli']:15}{student['student_code']:15}")
                i += 1
            print("---------------------------------------------------------------------------")
            success_jingle()
            input("Press any key ...")


        case _:
            print("! ! ! Undefined Choice ! ! !")
            print("---------------------------------------------------------------------------")
            fail_jingle()
            input("Press any key ...")
#-----------------------< Fancy Functions >-----------------------------
def startup_jingle():                                   #sound_effects
    Beep(2000,500)
    Beep(4000,250)
    Beep(3000,250)
    Beep(2000,250)



def success_jingle():
    Beep(2500,250)
    Beep(3000,250)
    Beep(3500,500)



def fail_jingle():
    Beep(150,500)




def quit_jingle():
    Beep(2000,250)
    Beep(3000,250)
    Beep(4000,250)
    Beep(2000,500)




# thread_running = True                                   #this part was for a waiting for an input animation/jingle

# def waiting_jingle():
#     global thread_running
#     while thread_running:
#         Beep(2000,500)
#         Beep(2500,500)
#         Beep(2000,500)
#         Beep(1500,500)

# def wait_animation():                     #a waiting animation I stole from stackoverflow                         
#     global thread_running
#     a = 0   
#     while thread_running:
#         b = ("Waiting" + "." * a)
#         a += 1  
#         stdout.write('\r'+b)
#         sleep(0.5)
#         if a >= 4:
#             a = 0

# def custom_input():
#     pass


#autosave func?

