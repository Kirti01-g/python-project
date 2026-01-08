import re
#express the regular expression for validating an Email
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    #if the string matches the regular expression, return True
    if re.match(regex, email):
        return True
    else:
        return False
    #test the function
    test_emails = ["test@example.com","invalid-email","user.name@domain.com"]

    for email in test_emails:
        if is_valid_email(email):
            print(f"{email} is a valid email address.")
        else:
            print(f"{email} is not a valid email address.")

            #output
user_input = input("Enter an email address to validate: ")
if is_valid_email(user_input):
    print(f"{user_input} is a valid email address.")
else:
    print(f"{user_input} is not a valid email address.")