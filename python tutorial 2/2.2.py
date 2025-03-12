def remove_odd_index(s):
    return ''.join([char for index, char in enumerate(s) if index % 2 == 0])
s = input("Enter a string: ")
print("String after removing characters at odd index positions:", remove_odd_index(s))