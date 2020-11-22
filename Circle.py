from Shape import Shape
from Vector import Vector

class Circle(Shape):
    def __init__(self,figure_name, radius):
        try:
            if float(radius) <= 0:
                raise ValueError("Radius must be positive.")
            super().__init__(figure_name)
            self.radius = float(radius)
        except ValueError as ve:
            raise ve

    def scale(self, ratio):
        self.radius = float(ratio) * self.radius

    def draw(self):
        print("CIRCLE")
        self.display()
        print("\nRADIUS R: "+str(self.radius))
