scores = [45, 88, 72, 31, 95, 60]
binned_data = []

for s in scores:
    if s < 50: binned_data.append("Low")
    elif s < 80: binned_data.append("Medium")
    else: binned_data.append("High")

print(f"Scores: {scores}")
print(f"Categories: {binned_data}")
