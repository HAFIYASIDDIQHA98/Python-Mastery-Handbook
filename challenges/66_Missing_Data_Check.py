data = [10, None, 20, None, 30]
missing_indices = [i for i, v in enumerate(data) if v is None]
print("Missing at indices:", missing_indices)
