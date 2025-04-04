n = int(input());
i = 2; factors = [];
while i * i <= n: n, factors = (n // i, factors + [i]) if n % i == 0 else (n, factors);
print(factors + [n] if n > 1 else factors)