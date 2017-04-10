class Circle(object):
    #class object attributes
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * Circle.pi

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_radius(self):
        return self.radius

    def perimeter(self):
        return 2 * Circle.pi * self.radius

c = Circle(100)
print(c)
print(c.pi)
print(c.radius)
print(c.area())
print(c.set_radius(10))
print(c.radius)
print(c.get_radius())



