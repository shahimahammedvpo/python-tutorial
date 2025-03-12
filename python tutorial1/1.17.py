def multiplication_tables(n):
    for i in range(1, n+1):
        print(f"Multiplication table for {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")
        print()
try:
    n = int(input("Enter a number n: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        multiplication_tables(n)
except ValueError:
    print("Invalid input. Please enter a positive integer.")