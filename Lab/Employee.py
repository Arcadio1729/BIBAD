from College import CollegeUser

class Employee(CollegeUser):
    def __init__(self,firstname,lastname,emailaddress,roomnr):
        CollegeUser.__init__(self,firstname,lastname,emailaddress)
        self.roomnr=roomnr
        self.grades=dict
        self.inbox=[]