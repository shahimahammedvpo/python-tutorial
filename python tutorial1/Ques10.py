n = int(input());
print(sum(int(input()) for _ in range(n) if _ % 2 == 0))