n = int(input("Enter the no: of need table upto : "))
for i in range(1, n+1):
print(f"Multiplication table of {i}:")
for j in range(1, 11):
print(f"{i} x {j} = {i * j}")
print()