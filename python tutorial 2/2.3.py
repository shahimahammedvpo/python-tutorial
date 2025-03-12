def is_palindrome(s):
    return all(s[i] == s[-(i + 1)] for i in range(len(s)//2))
s = input("Enter a string: ")
if is_palindrome(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")