def sum_of_digits_is_divisible_by_9(n):
    return sum(int(digit) for digit in str(n)) % 9 == 0
print("Numbers between 100 and 1000 whose sum of digits is divisible by 9:")
for num in range(100, 1000):
    if sum_of_digits_is_divisible_by_9(num):
        print(num, end=' ')