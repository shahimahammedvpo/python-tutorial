def print_pattern():
    for i in range(5, 0, -1):
        print(" ".join(map(str, range(i, 0, -1))))
print_pattern()