from LibraryManager import LibraryManager
from Reader import Reader
from Employee import Employee

def print_list(lst):
    [print(l) for l in lst]

def enter_command(user_type,command_name,lu,parameters):    # niejasna nazwa lu
    if lu.get_user_type()=='EMPLOYEE':
        if command_name=='0':
            return False
        if command_name=='1':
            print("Enter new reader id:")
            new_user_id = input()
            if lu.add_new_user(new_user_id, "READER"):
                print("User " + new_user_id + " added as READER successfully!")
            else:
                print("You cannot add this user. User " + new_user_id + " already exists in database.")
            return True

        if command_name=='2':
            print("Enter Title:")
            new_book_title = input()
            print("Enter Author:")
            new_book_author = input()
            print("Enter ID:")
            new_book_id = input()
            print("Enter Year:")
            new_book_year = input()

            if lu.add_new_book(new_book_id, new_book_title, new_book_author, new_book_year):
                print("Book has been added successfully!")
            else:
                print("You cannot add this book. Book with id: "+new_book_id+" already exists in database library.")
            return True

        if command_name=='3':
            print("Enter book:")
            book_criteria=input()
            found_books = lu.find_book(book_criteria)
            if found_books != []:
                print_list(found_books)
            else:
                print("None books has been found.")
            return True

        if command_name=='4':
            lu.approve_return()

        print(command_name+" is unknown. Please use one of the below options:")
        print_instructions("EMPLOYEE")
        return True

    if lu.get_user_type()=='READER':
        if command_name=='0':
            return False
        if command_name=='1':
            print("Enter book:")
            book_criteria=input()
            found_books = lu.find_book(book_criteria)
            if found_books != []:
                print_list(found_books)
            else:
                print("None books has been found.")
            return True

        if command_name=='2':
            print("Enter book id:")
            book_id=input()
            lu.borrow_book(book_id)
            return True
        if command_name=='3':
            print("Enter book id")
            book_id=input()
            lu.return_book(book_id)
            return True
        print(command_name+" is unknown. Please use one of the below options:")
        print_instructions("READER")
        return True


def print_instructions(user_type):
    if user_type.upper()=="EMPLOYEE":
        print("MENU\n")
        print("0 - Log out")
        print("1 - Add new reader")
        print("2 - Add new book")
        print("3 - Find books")
        print("4 - Approve returns")
        print("\n------EMPLOYEE PANEL-------")
    if user_type.upper()=="READER":
        print("MENU\n")
        print("0 - Log out")
        print("1 - Find books")
        print("2 - Borrow book.")
        print("3 - Return book.")
        print("\n------READER PANEL-------")

if __name__ == "__main__":

    users_source_path="users.json"
    books_source_path="books_library_base.json"
    waiting_source_path="books_waiting_room.json"
    program_running=True

    while program_running:
        print("Welcome in LMS (LIBRARY MANAGEMENT SYSTEM).")
        print("Enter your login ID:")

        input_login_id = str(input())
        lm = LibraryManager(users_source_path,books_source_path,waiting_source_path)

        input_login_type=lm.get_user_by_id(input_login_id)

        if(input_login_type=="READER"):
            output_message="Welcome in READER PANEL"
            lu=Reader(input_login_id,lm)
        elif(input_login_type=="EMPLOYEE"):
            output_message="Welcome in EMPLOYEE PANEL"
            lu=Employee(input_login_id,lm)

        print("Hi "+input_login_id)
        print(output_message)
        print_instructions(input_login_type)
        logged_in=True
        while logged_in:
            print("Enter command:")

            current_input_command=str(input())
            current_command_with_parameters=current_input_command.split(" ")

            current_command_name=current_command_with_parameters[0]
            current_command_parameters=current_command_with_parameters[1:]

            logged_in=enter_command(lu.get_user_type(),current_command_name,lu,current_command_parameters)
