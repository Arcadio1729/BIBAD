from Employee import Employee

class Profesor(Employee):
    def __init__(self,firstname,lastname,emailaddress,roomnr):
        Employee.__init__(self,firstname,lastname,emailaddress,roomnr)
        self.publications=[]

    def addPublication(self,content):
        self.publications.append(content)