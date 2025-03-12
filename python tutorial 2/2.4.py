def replace_spaces(s):
    if ' ' in s:
        return s.replace(' ', '*')
    else:
        return f"${s}$"
s = input("Enter a string: ")
print("Modified string:", replace_spaces(s))