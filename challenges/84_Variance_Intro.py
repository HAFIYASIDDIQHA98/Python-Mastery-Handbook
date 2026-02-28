data = [2, 4, 4, 4, 5, 5, 7, 9]
mean = sum(data) / len(data)

# Sum of squared differences from the mean
variance = sum((x - mean) ** 2 for x in data) / len(data)

print(f"Mean: {mean}")
print(f"Variance: {variance:.2f}")
