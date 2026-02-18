user = {"id": 101, "name": "Hafiya", "role": "Dev"}
key = input("Enter key to search: ")
if key in user:
    print(f"Value: {user[key]}")
else:
    print(f"Key '{key}' not found!")
