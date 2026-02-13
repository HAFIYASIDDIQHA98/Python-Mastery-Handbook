bill = float(input("Total Bill: $"))
tip_percent = int(input("Tip percentage (10, 12, 15): "))
people = int(input("Number of people: "))

total = bill * (1 + tip_percent / 100)
per_person = total/people

print(f"Each person should pay: ${per_person:.2f}")
