def compute_expression(n):
    return 2**(2*n) + n + 5
try:
    n = int(input("Enter a positive integer n: "))
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        result = compute_expression(n)
        print(f"The result of 2^(2*{n}) + {n} + 5 is: {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")