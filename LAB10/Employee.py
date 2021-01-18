import json
from LibraryManager import LibraryManager
from LibraryUser import LibraryUser
from Book import Book
from Reader import Reader

class Employee(LibraryUser):

    def __init__(self,user_id,lm):
        super().__init__(user_id,"EMPLOYEE",lm)

    def add_new_user(self,user_id,user_type):
        return self.lm.add_new_user(user_id,user_type)

    def add_new_book(self, book_id, book_title,book_author,book_year):
        return self.lm.add_new_book(book_id,book_title,book_author,book_year)

    def approve_return(self):   # zwrot czego?
        return self.lm.approve_return()
