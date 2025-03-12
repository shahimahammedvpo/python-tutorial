def sum_of_odds(lower, upper):
    return sum(num for num in range(lower, upper+1) if num % 2 != 0)
try:
    lower, upper = map(int, input("Enter the lower and upper limits (separated by space): ").split())
    if lower > upper:
        print("Lower limit cannot be greater than upper limit.")
    else:
        result = sum_of_odds(lower, upper)
        print(f"The sum of odd numbers between {lower} and {upper} is: {result}")
except ValueError:
    print("Invalid input. Please enter integer values for limits.")