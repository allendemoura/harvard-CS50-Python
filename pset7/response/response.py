import validators

status = validators.email(input("What's your email address? "))

print("Valid" if status else "Invalid")
