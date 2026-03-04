# Automatically removing data points that are too high
data = [20, 22, 21, 23, 150, 22, 24] # 150 is the outlier
threshold = 100

clean_data = [x for x in data if x < threshold]

print(f"Original Data: {data}")
print(f"Cleaned Data (Outliers Removed): {clean_data}")
