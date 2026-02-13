email = input("Enter your email: ").strip()
username = email[:email.index("@")]
domain = email[email.index("@")+1:]

print(f"Username: {username}")
print(f"Domain: {domain}")
