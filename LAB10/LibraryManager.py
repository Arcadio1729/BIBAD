import json
import re
from Book import Book

class LibraryManager:

    def __init__(self,users_source_path,books_source_path,waiting_source_path):
        self._users={}
        self._books={}
        self._waitings={}

        self._users_source_path=users_source_path
        self._books_source_path=books_source_path
        self._waiting_source_path=waiting_source_path

    def __read_data_from_json(self,json_path):
        with open(json_path,"r") as f:
            json_object=json.load(f)
            f.close()
        return json_object

    def __write_data_to_json(self,json_path,json_data):
        with open(json_path,"w") as f:
            json.dump(json_data,f)
            f.close()

    def get_users(self):
        self._users=self.__read_data_from_json(self._users_source_path)

    def get_books(self):
        self._books = self.__read_data_from_json(self._books_source_path)

    def get_waitings(self):
        self._waitings = self.__read_data_from_json(self._waiting_source_path)


    def add_new_user(self, user_id, user_type):
        self.get_users()
        json_user_object={}
        if not self._users.keys().__contains__(user_id):
            user_object = {"user_id": user_id, "user_type": user_type, "borrowed_books": []}
            self._users[user_id]=user_object
            self.__write_data_to_json(self._users_source_path,self._users)
            return True
        else:
            return False

    def drop_user(self, user_id):
        self.get_users()
        self._books.pop(user_id)
        self.__write_data_to_json(self._users_source_path,self._users)
        return True

    def add_new_book(self, book_id, book_title,book_author,book_year):
        self.get_books()
        json_book_object={}
        if not self._books.keys().__contains__(book_id):
            book_object = {"ID": book_id, "Title": book_title, "Author": book_author,"Year":book_year,"Available":True,"Reader":''}
            self._books[book_id]=book_object
            self.__write_data_to_json(self._books_source_path,self._books)
            return True
        else:
            return False

    def drop_book(self, book_id):
        self.get_books()
        self._books.pop(book_id)
        self.__write_data_to_json(self._books_source_path,self._books)
        return True


    def find_book(self, search_name):
        found_books = []
        self.get_books()
        found_books += self.__find_book_by_title(search_name)
        found_books += self.__find_book_by_author(search_name)
        found_books += self.__find_book_by_ID(search_name)

        return found_books


    def __find_book_by_ID(self,id_name):
        found_books=[]
        if self.book_exists(id_name):
            if self._books[id_name]["Available"]==True:
                found_books.append(Book(id_name,self._books[id_name]["Title"],self._books[id_name]["Author"],self._books[id_name]["Year"]))
        return found_books

    def __find_book_by_title(self, title_name):
        found_books = []

        for b in self._books.values():
            if not re.search(title_name.upper(), b["Title"].upper()) == None:
                if b["Available"] == True:
                    found_books.append(Book(b["ID"], b["Title"], b["Author"], b["Year"]))

        return found_books

    def __find_book_by_author(self, author_name):
        found_books = []

        for b in self._books.values():
            if not re.search(author_name.upper(), b["Author"].upper()) == None:
                if b["Available"] == True:
                    found_books.append(Book(b["ID"], b["Title"], b["Author"], b["Year"]))
        return found_books


    def approve_return(self):
        self.get_waitings()
        self.get_users()
        self.get_books()

        returned_books=[]

        for k in self._waitings.keys():
            self._books[k]["Available"]=True
            current_user=self._books[k]["Reader"]
            self._users[current_user]["borrowed_books"].remove(k)
            self._books[k]["Reader"]=""
            returned_books.append(k)

        self._waitings.clear()
        self.__write_data_to_json(self._waiting_source_path,self._waitings)
        self.__write_data_to_json(self._books_source_path,self._books)
        self.__write_data_to_json(self._users_source_path,self._users)

        return True

    def borrow_book(self,book_id,user_id):
        self.get_books()
        self._books[book_id]["Available"]=False
        self._books[book_id]["Reader"]=user_id


        self.__write_data_to_json(self._books_source_path,self._books)
        self.get_users()
        self._users[user_id]["borrowed_books"].append(book_id)

        self.__write_data_to_json(self._users_source_path,self._users)

        return True


    def return_book(self,book_id,user_id):
        self.get_users()
        self.get_waitings()
        self.get_books()

        book_object = {"ID": self._books[book_id]["ID"], "Title": self._books[book_id]["Title"], "Author": self._books[book_id]["Author"],"Year":self._books[book_id]["Year"],"Available":True,"Reader":''}
        self._waitings[book_id]=book_object

        self.__write_data_to_json(self._waiting_source_path,self._waitings)

    def user_exists(self,user_id):
        for key in self._users.keys():
            if key==user_id:
                return True
        return False

    def book_exists(self,book_id):
        self.get_books()
        if bool(self._books):
            return False
        for key in self._books.keys():
            if key==book_id:
                return True
        return False

    def get_user_by_id(self,user_id):
        self.get_users()
        for k in self._users.keys():
            if k==user_id:
                return self._users[user_id]["user_type"]
        return null
