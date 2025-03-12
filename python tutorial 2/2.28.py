def sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

sort_list(numbers)
print(f"Sorted list: {numbers}")