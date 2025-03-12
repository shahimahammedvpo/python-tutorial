import math

def area_of_circle(radius):
    return math.pi * radius ** 2
radius = float(input("Enter the radius of the circle: "))
print(f"The area of the circle is: {area_of_circle(radius)}")