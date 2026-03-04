# Scaling data between 0 and 1
data = [100, 200, 300, 400, 500]
min_val = min(data)
max_val = max(data)

normalized = [(x - min_val) / (max_val - min_val) for x in data]

print(f"Original: {data}")
print(f"Normalized (0-1): {normalized}")
