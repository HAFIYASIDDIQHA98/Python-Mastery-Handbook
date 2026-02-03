# Program to manage and search Employee Records
employees = {
    101: {"name": "Hafiya", "role": "Python Developer", "salary": 75000},
    102: {"name": "Ali", "role": "Data Analyst", "salary": 65000},
    103: {"name": "Sara", "role": "Manager", "salary": 90000}
}

emp_id = int(input("Enter Employee ID to search (101-103): "))

# Logic to check if ID exists and print details
if emp_id in employees:
    record = employees[emp_id]
    print(f"--- Record Found ---")
    print(f"Name: {record['name']}")
    print(f"Role: {record['role']}")
    print(f"Salary: {record['salary']}")
else:
    print("Error: Employee ID not found in our database.")
