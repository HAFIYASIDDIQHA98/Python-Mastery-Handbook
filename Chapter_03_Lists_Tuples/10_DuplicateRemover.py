
raw_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
unique_list = []

for item in raw_list:
    if item not in unique_list:
        unique_list.append(item)

print(f"Original List: {raw_list}")
print(f"Cleaned List: {unique_list}")
