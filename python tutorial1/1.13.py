def reverse_number(n):
    return int(str(n)[::-1])
try:
    n = int(input("Enter an integer: "))
    reversed_n = reverse_number(n)
    print(f"The reverse of {n} is {reversed_n}")
except ValueError:
    print("Invalid input. Please enter an integer.")