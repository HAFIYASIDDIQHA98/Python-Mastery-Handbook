# Adding data without deleting old content
f = open("new_file.txt", "a") # 'a' means Append mode
f.write("\nThis line is appended at the end.")
f.close()
