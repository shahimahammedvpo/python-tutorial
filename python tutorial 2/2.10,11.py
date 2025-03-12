import re

def is_valid_password(password):
    if len(password) >= 6:
        if re.search("[a-z]", password) and re.search("[0-9]", password) and re.search("[A-Z]", password) and re.search("[$#@]", password):
            return True
    return False
password = input("Enter a password: ")
if is_valid_password(password):
    print("The password is valid.")
else:
    print("The password is not valid.")
    def decimal_to_binary(n):
    return bin(n)[2:]
n = int(input("Enter a decimal number: "))
print(f"The binary representation of {n} is:", decimal_to_binary(n))