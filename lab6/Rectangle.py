from Vector import Vector
from Shape import Shape

class Rectangle(Shape):
    #figure size is the pair of two sides

    def __init__(self,figure_name,side_a,side_b):
        super().__init__(figure_name)
        self.side_a=float(side_a)
        self.side_b=float(side_b)

    def scale(self,ratio):
        try:
            self.side_a=ratio*self.side_a
            self.side_b=ratio*self.side_b
        except ValueError:
            raise ValueError("Invalid angle input. Ratio should be numeric format.")

    def draw(self):
        print("RECTANGLE")
        self.display()
        print("SIDE A: "+str(self.side_a))
        print("SIDE B: "+str(self.side_b))