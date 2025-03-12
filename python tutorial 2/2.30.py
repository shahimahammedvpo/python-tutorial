def remove_duplicates(numbers):
    return list(set(numbers))

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = remove_duplicates(numbers)
print(f"List without duplicates: {unique_numbers}")