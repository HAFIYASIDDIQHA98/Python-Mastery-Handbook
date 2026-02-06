def backup_data(source, target):
    with open(source, "r") as f:
        content = f.read()
    
    with open(target, "w") as f:
        f.write(content)
    
    print(f"Backup successful from {source} to {target}")

# Usage
backup_data("data.txt", "backup_data.txt")
