data = {'Python': 8, 'SQL': 5, 'Java': 3, 'DS': 7}

print("Skill Frequency Chart:")
for skill, count in data.items():
    print(f"{skill:10}: {'#' * count} ({count})")
