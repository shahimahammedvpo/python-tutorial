def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit)**num_digits for digit in num_str)
    return sum_of_powers == num
try:
    n = int(input("Enter an integer: "))
    if is_armstrong_number(n):
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is not an Armstrong number.")
except ValueError:
    print("Invalid input. Please enter an integer.")