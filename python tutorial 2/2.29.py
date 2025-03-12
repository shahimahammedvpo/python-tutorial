set1 = set(map(int, input("Enter elements of set1 separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements of set2 separated by spaces: ").split()))

union_set = set1 | set2
print(f"Union: {union_set}")

intersection_set = set1 & set2
print(f"Intersection: {intersection_set}")

difference_set = set1 - set2
print(f"Difference (set1 - set2): {difference_set}")

symmetric_difference_set = set1 ^ set2
print(f"Symmetric Difference: {symmetric_difference_set}")