def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
fib_numbers = fibonacci_sequence(10)
print("First 10 Fibonacci numbers:", fib_numbers)