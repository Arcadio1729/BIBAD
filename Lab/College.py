class CollegeUser(object):
    def __init__(self,firstname,lastname,emailaddress):
        self.firstname=firstname
        self.lastname=lastname
        self.emailaddress=emailaddress

    def sendEmail(self,content):
        self.inbox.append(content)
