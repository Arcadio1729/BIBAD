from Lab import College

class Student(CollegeUser):
    def __init__(self,firstname,lastname,emailaddress,indexnumber):
        CollegeUser.__init__(self,firstname,lastname,emailaddress)
        self.indexnumber=indexnumber
        self.grades={"":0}
        self.inbox=[]

    def addGrade(self,subject,grad):
        self.grades[subject]=grad

