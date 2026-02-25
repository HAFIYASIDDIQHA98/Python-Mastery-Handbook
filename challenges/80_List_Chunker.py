data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3

# Splitting data into chunks of 3
chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

print(f"Full Data: {data}")
print(f"Data Batches: {chunks}")
