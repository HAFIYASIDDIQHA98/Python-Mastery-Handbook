email = input("Enter email: ")
if "@" in email and "." in email:
    if email.find("@") < email.rfind("."):
        print("Valid Email")
    else:
        print("Invalid Format")
else:
    print("Invalid Email")
