def compute_sums_and_averages(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    negative_numbers = [num for num in numbers if num < 0]
    
    sum_positive = sum(positive_numbers)
    sum_negative = sum(negative_numbers)
    
    avg_positive = sum_positive / len(positive_numbers) if positive_numbers else 0
    avg_negative = sum_negative / len(negative_numbers) if negative_numbers else 0
    
    return sum_positive, sum_negative, avg_positive, avg_negative
try:
    numbers = [int(input(f"Enter integer {i+1}: ")) for i in range(4)]
    sum_positive, sum_negative, avg_positive, avg_negative = compute_sums_and_averages(numbers)
    print(f"Sum of positive numbers: {sum_positive}")
    print(f"Sum of negative numbers: {sum_negative}")
    print(f"Average of positive numbers: {avg_positive}")
    print(f"Average of negative numbers: {avg_negative}")
except ValueError:
    print("Invalid input. Please enter integers only.")