import json
from LibraryUser import LibraryUser
from LibraryManager import LibraryManager

class Reader(LibraryUser):
    def __init__(self,user_id,lm):
        super().__init__(user_id,"READER",lm)

    def borrow_book(self,book_id):
        return self.lm.borrow_book(book_id,self._user_id)

    def return_book(self,book_id):
        return self.lm.return_book(book_id,self._user_id)
