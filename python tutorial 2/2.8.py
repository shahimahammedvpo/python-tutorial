def replace_substring(s, old, new):
    return s.replace(old, new)
s = input("Enter a string: ")
old = input("Enter substring to replace: ")
new = input("Enter new substring: ")
print("Modified string:", replace_substring(s, old, new))