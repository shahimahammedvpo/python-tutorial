n = int(input("Enter the number of elements: "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
even_sum = sum(num for num in numbers if num % 2 == 0)
print(f"The sum of even numbers is: {even_sum}")