# Reading file line by line
f = open("sample.txt", "r")
line1 = f.readline() # Reads first line
line2 = f.readline() # Reads second line
print(line1, end="")
print(line2)
f.close()
