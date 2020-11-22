from Vector import Vector

class Shape:
    def __init__(self,figure_name):
        try:
            self.colors = ["black", "white", "red", "green", "blue", "cyan", "magneta", "yellow"]
            self.figure_name = str(figure_name)
            self.middle_point = Vector(0, 0)
            self.rotation = 0
            self.background_color="white"
            self.border_color="black"
        except ValueError as ve:
            raise ve

    def draw(self):
        pass

    def rotate(self, angle):
        try:
            self.rotation = self.rotation + float(angle)
        except ValueError as ve:
            raise ve

    def move(self, vector):
        try:
            if type(vector) is Vector:
                self.middle_point = self.middle_point + vector
            else:
                raise ValueError("Move vector should be Vector type")
        except ValueError as ve:
            raise ve

    def set_border_color(self, color):
        try:
            if color not in self.colors:
                raise ValueError('Border color should be from list ' + str(self.colors))
            self.border_color = color
        except ValueError as ve:
            raise ve

    def set_background_color(self, color):
        try:
            if color not in self.colors:
                raise ValueError('Background color should be from list ' + str(self.colors))
            self.background_color = color
        except ValueError as ve:
            raise ve

    def display(self):
        print(self.figure_name+"\nbackground-color: "+self.background_color+"\nborder-color: "+self.border_color+"\nrotation: "+str(self.rotation)+"\nmiddle: "+str(self.middle_point))