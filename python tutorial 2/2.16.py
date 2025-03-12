import math

def sin_x(x, n):
    result = 0
    for i in range(n):
        sign = (-1) ** i
        result += sign * (x ** (2*i + 1)) / math.factorial(2*i + 1)
    return result
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms: "))
print(f"sin({x}) = {sin_x(x, n)}")