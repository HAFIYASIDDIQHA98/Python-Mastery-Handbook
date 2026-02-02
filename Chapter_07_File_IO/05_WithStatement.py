# The best way to handle files (Auto-close)
with open("sample.txt", "r") as f:
    print(f.read())
# No need to call f.close() - it's automatic!
