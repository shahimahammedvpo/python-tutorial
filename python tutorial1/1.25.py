def power(x, y):
    result = 1
    for _ in range(abs(y)):
        result *= x
    if y < 0:
        result = 1 / result
    return result
try:
    x = float(input("Enter the base number (X): "))
    y = int(input("Enter the exponent (Y): "))
    result = power(x, y)
    print(f"{x} raised to the power of {y} is: {result}")
except ValueError:
    print("Invalid input. Please enter numerical values.")