def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def separate_prime_composite(numbers):
    primes, composites = [], []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
        else:
            composites.append(num)
    return primes, composites

numbers = list(map(int, input("Enter positive integers separated by spaces: ").split()))

primes, composites = separate_prime_composite(numbers)
print(f"Prime numbers: {primes}")
print(f"Composite numbers: {composites}")