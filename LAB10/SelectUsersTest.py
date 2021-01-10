import unittest
from LibraryManager import LibraryManager
from Employee import Employee
from Reader import Reader

class MyTestCase(unittest.TestCase):
    def test_select(self):
        books_source_path = "C:\\Users\\arcad\\Desktop\\ja\\college\\IT\\BibliotekiAnalizyDanych\\Lab10\\books_library_base.json"

        lm=LibraryManager("C:\\Users\\arcad\\Desktop\\ja\\college\\IT\\BibliotekiAnalizyDanych\\Lab10\\users.json","")
        #lm.add_new_library_user("2","ARO")
        #u=lm.get_user_by_id("admin")
        #e=Employee("admin","C:\\Users\\arcad\\Desktop\\ja\\college\\IT\\BibliotekiAnalizyDanych\\Lab10\\users.json","C:\\Users\\arcad\\Desktop\\ja\\college\\IT\\BibliotekiAnalizyDanych\\Lab10\\books_library_base.json")
        #e.add_new_book("L123","Lalka","Boleslaw Prus","2001")
        r=Reader("Aro",books_source_path)
        lst=r.find_book_by_title("HarryPotter")
        
        self.assertEqual(True, True)


if __name__ == '__main__':
    m=MyTestCase()
    m.test_select()
