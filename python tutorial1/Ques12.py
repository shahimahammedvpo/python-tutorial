nums = [int(input()) for _ in range(4)];
pos = [x for x in nums if x > 0];
neg = [x for x in nums if x < 0];
print(sum(pos), sum(neg), sum(pos)/len(pos) if pos else 0, sum(neg)/len(neg) if neg else 0)