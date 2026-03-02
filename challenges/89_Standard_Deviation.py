import math
data = [10, 12, 23, 23, 16, 23, 21, 16]
mean = sum(data) / len(data)
variance = sum((x - mean) ** 2 for x in data) / len(data)
std_dev = math.sqrt(variance)

print(f"Dataset: {data}")
print(f"Standard Deviation: {std_dev:.2f}")
