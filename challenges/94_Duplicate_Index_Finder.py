# Finding where duplicates are located
data = [10, 20, 30, 20, 40, 50, 20]
target = 20

indices = [i for i, x in enumerate(data) if x == target]

print(f"Dataset: {data}")
print(f"Value '{target}' found at indices: {indices}")
