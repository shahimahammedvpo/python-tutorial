import math
a, b, c = map(float, input().split())
d = b**2-4*a*c;
if d >= 0:
print((-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a))
else:
print("No Real Roots")