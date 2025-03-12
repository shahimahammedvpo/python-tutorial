def count_even_odd(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    return even_count, odd_count
try:
    n = int(input("Enter the number of elements: "))
    numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
    even_count, odd_count = count_even_odd(numbers)
    print(f"Number of even numbers: {even_count}")
    print(f"Number of odd numbers: {odd_count}")
except ValueError:
    print("Invalid input. Please enter integers only.")