def remove_substring(s, sub):
    return s.replace(sub, '')
s = input("Enter a string: ")
sub = input("Enter substring to remove: ")
print("String after removing substring:", remove_substring(s, sub))