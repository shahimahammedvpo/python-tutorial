def prime_factors(n):
    while n % 2 == 0:
        print(2, end=' ')
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            print(i, end=' ')
            n = n // i
    if n > 2:
        print(n)
try:
    n = int(input("Enter a number to find its prime factors: "))
    if n <= 1:
        print("Please enter a number greater than 1.")
    else:
        print(f"Prime factors of {n} are:", end=' ')
        prime_factors(n)
except ValueError:
    print("Invalid input. Please enter a positive integer.")