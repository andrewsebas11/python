class Shape:
    def __init__(self, length, breadth, a, radius):
        self.length = length
        self.breadth = breadth
        self.a = a
        self.radius = radius

    def arearectangle(self):
        print(f"Area = {self.length * self.breadth}")

    def areasquare(self):
        print(f"Area = {self.a ** 4}")

    def areacircle(self):
        print(f"Area = {((self.radius) ** 2) * 3.14}")


s = Shape(4, 5, 6, 7)
s.arearectangle()
s.areasquare()
s.areacircle()