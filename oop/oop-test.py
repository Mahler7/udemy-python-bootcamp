####Problem 1 Fill in the Line class methods to accept coordinate as a pair of tuples and return the slope and distance of the line.
import math

class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        distance = math.sqrt((self.coor2[0] - self.coor1[0]) ** 2 + (self.coor2[1] - self.coor1[1]) ** 2)
        return distance
    
    def slope(self):
        slope = (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
        return slope

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())

#Fill in the class
class Cylinder(object):
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        volume = math.pi * self.radius ** 2 * self.height
        return volume
    
    def surface_area(self):
        surface_area = (2 * math.pi * self.radius * self.height) + (2 * math.pi * self.radius ** 2)
        return surface_area

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())