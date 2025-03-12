from collections import Counter

def find_mode(numbers):
    count = Counter(numbers)
    max_count = max(count.values())
    modes = [key for key, value in count.items() if value == max_count]
    return modes

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

modes = find_mode(numbers)
print(f"The mode(s): {', '.join(map(str, modes))}")