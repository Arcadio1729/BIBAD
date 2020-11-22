from Shape import Shape
from Vector import Vector

class Triangle(Shape):
    def __init__(self, figure_name, side_a, side_b, side_c):
        try:
            if float(side_a) <= 0 or float(side_b) <= 0 or float(side_c) <= 0:
                raise Exception("Side must be greater than 0.")
            if float(side_a) + float(side_b) <= float(side_c) or float(side_b) + float(side_c) <= float(side_a) or float(side_a) + float(side_c) <= float(side_b):
                raise Exception("Triangle condition has not been met.")

            super().__init__(figure_name)

            self.side_a = float(side_a)
            self.side_b = float(side_b)
            self.side_c = float(side_c)

        except Exception as e:
            raise e

    def scale(self, ratio):
        self.side_a = ratio * self.side_a
        self.side_b = ratio * self.side_b
        self.side_c = ratio * self.side_c

    def draw(self):
        print("TRIANGLE")
        self.display()
        print("SIDE A: "+str(self.side_a))
        print("SIDE B: "+str(self.side_b))
        print("SIDE C: "+str(self.side_c))