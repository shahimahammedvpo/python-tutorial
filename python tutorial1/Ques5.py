import math;
a, b, c = float(input()), float(input()), float(input());
d = b**2 - 4*a*c;
print(((-b + math.sqrt(d)) / (2*a), (-b - math.sqrt(d)) / (2*a)) if d >= 0 else "Complex roots")