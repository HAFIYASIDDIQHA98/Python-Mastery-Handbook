# Generates a table and saves it in a folder
num = int(input("Enter number for table: "))
table = ""
for i in range(1, 11):
    table += f"{num} X {i} = {num*i}\n"

with open(f"tables/Table_of_{num}.txt", "w") as f:
    f.write(table)
