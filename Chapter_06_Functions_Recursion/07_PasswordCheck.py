def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Use at least 8 characters"
    else:
        return "Strong Password"

# Testing
print(check_password_strength("hafiya123"))
print(check_password_strength("py"))
