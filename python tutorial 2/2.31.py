def remove_all_duplicates(numbers):
    count = {}
    for num in numbers:
        count[num] = count.get(num, 0) + 1
    return [num for num in numbers if count[num] == 1]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = remove_all_duplicates(numbers)
print(f"List without any duplicates: {unique_numbers}")