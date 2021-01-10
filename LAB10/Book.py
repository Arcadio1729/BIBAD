
class Book:
    def __init__(self,id,title,author,year):
        self.id=id
        self.title=title
        self.author=author
        self.year=year
        self.availability=True

    def __str__(self):
        return "Title: "+self.title+"\n Author: "+self.author+"\n Year:"+self.year+"\n ID: "+self.id+"\n"
    
    