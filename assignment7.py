import math
class polygon1:
def areasample(self):
pass
class rectangle(polygon1):
def __init__(self, length1, breadth1):
self.length = length1
self.width = breadth1
def areasample(self):
return self.length * self.width
class circle(polygon1):
def __init__(self, radius1):
self.radius = radius1
def areasample(self):
return math.pi * self.radius**2

p = float(input("Enter the length of the rectangle: "))
q = float(input("Enter the breadth of the rectangle: "))
r = float(input("Enter the radius of circle: "))
sample = circle(r)
print("Area of circle is: ", sample.areasample())
sample2 = rectangle(p, q)

print("Area of rectangle is: ", sample2.areasample())
