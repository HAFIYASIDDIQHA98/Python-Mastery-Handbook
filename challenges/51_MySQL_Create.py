# Conceptual Database Logic
table_name = "Projects"
columns = "(id INT, title VARCHAR(100), status VARCHAR(20))"
query = f"CREATE TABLE {table_name} {columns};"
print("Generated SQL Query:", query)
