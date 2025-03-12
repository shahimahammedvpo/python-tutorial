def compare_numbers(num1, num2):
    if num1 == num2:
        return f"{num1} and {num2} are equal."
    elif num1 > num2:
        return f"{num1} is greater than {num2}."
    else:
        return f"{num1} is less than {num2}."
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    print(compare_numbers(number1, number2))
except ValueError:
    print("Invalid input. Please enter numeric values.")