from Employee import Employee


class Teacher(Employee):
    def __init__(self,firstname,lastname,emailaddress,roomnr):
        Employee.__init__(self,firstname,lastname,emailaddress,roomnr)
        self.subjects = []
        self.consultations={}

    def addPublication(self, content):
        self.subjects.append(content)
