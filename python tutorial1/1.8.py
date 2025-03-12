def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))
try:
    num = int(input("Enter a number: "))
    result = sum_of_digits(num)
    print(f"The sum of the digits of {num} is: {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")