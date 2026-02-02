# Reading an existing file
f = open("sample.txt", "r") # 'r' means Read mode
data = f.read()
print(data)
f.close()
