def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "Quadrant I"
    elif x < 0 and y > 0:
        return "Quadrant II"
    elif x < 0 and y < 0:
        return "Quadrant III"
    elif x > 0 and y < 0:
        return "Quadrant IV"
    elif x == 0 and y == 0:
        return "Origin"
    elif x == 0:
        return "On the y-axis"
    else:
        return "On the x-axis"
try:
    x = float(input("Enter x-coordinate: "))
    y = float(input("Enter y-coordinate: "))
    position = find_quadrant(x, y)
    print(f"The point ({x}, {y}) is at: {position}")
except ValueError:
    print("Invalid input. Please enter numeric values.")