import validators

#email_address = validators.email("john@gmail.com")
#print(email_address)

email_address = input("What's your email address? ")

is_valid = validators.email(email_address)


if is_valid == True:
    print("Valid")
else:
    print("Invalid")
