import re

def validate_password(password):
    pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if re.match(pattern, password):
        return True
    else:
        return False

pwd=input("Enter the password: ")
if validate_password(pwd):
    print("Valid password")
else:
    print("Invalid password")