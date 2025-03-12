import math
def calculate_circle_properties(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return area, circumference
radius = float(input("Enter the radius of the circle: "))
if radius < 0:
    print("Radius cannot be negative. Please enter a positive number.")
else:
    area, circumference = calculate_circle_properties(radius)
    print(f"Area of the circle: {area:.2f}")
    print(f"Circumference of the circle: {circumference:.2f}")