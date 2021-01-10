import json
from abc import ABC
from Book import Book
import re

class LibraryUser(ABC):

    def __init__(self,user_id,user_type,lm):
        self.lm=lm
        self._user_id=user_id
        self._user_type=user_type

        
    def log_in(self):
        pass

    def get_user_id(self):
        return self._user_id

    def get_user_type(self):
        return self._user_type

    def find_book(self,search_name):
        return self.lm.find_book(search_name)


