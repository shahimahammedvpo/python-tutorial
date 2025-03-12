import cmath
def find_quadratic_roots(a, b, c):
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    return root1, root2
try:
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    if a == 0:
        print("Coefficient 'a' cannot be zero.")
    else:
        root1, root2 = find_quadratic_roots(a, b, c)
        print(f"The roots of the quadratic equation are: {root1} and {root2}")
except ValueError:
    print("Invalid input. Please enter numeric values.")