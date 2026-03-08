# Formatting data for Excel/CSV export
users = [
    {"name": "Hafiya", "score": 95},
    {"name": "Python", "score": 88}
]

print("CSV Format:")
print("Name,Score") # Header
for user in users:
    print(f"{user['name']},{user['score']}")
