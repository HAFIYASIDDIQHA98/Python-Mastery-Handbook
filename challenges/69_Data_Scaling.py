# Task 69: Basic Normalization
scores = [100, 200, 300, 400, 500]
max_val = max(scores)

# Divide each number by the maximum value
normalized = [s / max_val for s in scores]

print(f"Scaled Scores: {normalized}")
