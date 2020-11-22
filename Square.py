from Rectangle import Rectangle
from Shape import Shape
from Vector import Vector

class Square(Rectangle):
    # figure size is the pair of two sides

    def __init__(self, figure_name, side_a):
        super().__init__(figure_name, side_a, side_a)

    def draw(self):
        print("SQUARE")
        self.display()
        print("SIDE A: "+str(self.side_a))