password = "SecretPassword123"
masked = "*" * (len(password) - 2) + password[-2:]
print("Masked:", masked)
