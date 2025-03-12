import cmath
def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    return root1, root2
try:
    a, b, c = map(float, input("Enter coefficients a, b, c of the quadratic equation (ax^2 + bx + c = 0): ").split())
    if a == 0:
        print("Coefficient 'a' cannot be zero.")
    else:
        root1, root2 = find_roots(a, b, c)
        print(f"The roots of the equation are: {root1} and {root2}")
except ValueError:
    print("Invalid input. Please enter numerical values for coefficients.")