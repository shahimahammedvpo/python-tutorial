def is_right_angled_triangle(a, b, c):
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2
try:
    side1 = float(input("Enter length of first side: "))
    side2 = float(input("Enter length of second side: "))
    side3 = float(input("Enter length of third side: "))
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("Side lengths must be positive numbers.")
    else:
        if is_right_angled_triangle(side1, side2, side3):
            print("The triangle is right-angled.")
        else:
            print("The triangle is not right-angled.")
except ValueError:
    print("Invalid input. Please enter positive numeric values.")