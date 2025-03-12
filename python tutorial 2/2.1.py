def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in s if char not in vowels])
s = input("Enter a string: ")
print("String without vowels:", remove_vowels(s))