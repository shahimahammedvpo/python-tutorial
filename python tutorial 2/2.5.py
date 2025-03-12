def slice_string(s):
    even_indices = s[::2]
    odd_indices = s[1::2]
    return even_indices, odd_indices
s = input("Enter a string: ")
even, odd = slice_string(s)
print("Even indices characters:", even)
print("Odd indices characters:", odd)