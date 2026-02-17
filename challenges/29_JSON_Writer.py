import json
data = {"Name": "Hafiya", "Role": "Python Developer", "Status": "Active"}
with open("profile.json", "w") as f:
    json.dump(data, f)
print("JSON file created!")
