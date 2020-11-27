class Vector:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, k): # jeszcze rmul by się przydało do kompletu
        new_x = (self.x) * k
        new_y = (self.y) * k
        return Vector(new_x, new_y)

    def __floordiv__(self, k):  # czemu floordiv, a nie div?
        new_x = self.x / k
        new_y = self.y / k
        return Vector(new_x, new_y)

    def __str__(self):
        return "(" + str(round(self.x, 2)) + "," + str(round(self.y, 2)) + ")"

    def rotate(self, angle):
        cos_angle = float(math.cos(angle))  # NameError
        sin_angle = float(math.sin(angle))

        new_x = (self.x) * cos_angle - (self.y) * sin_angle
        new_y = (self.x) * sin_angle + (self.y) * cos_angle

        return Vector(new_x, new_y)

    def norm(self):
        return float(math.sqrt(self.x ** 2 + self.y ** 2))
