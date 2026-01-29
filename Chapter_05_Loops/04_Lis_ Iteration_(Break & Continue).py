# Demonstrating break and continue
fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]

print("Iterating through the list:")
for fruit in fruits:
    if fruit == "Cherry":
        print("Skipping Cherry (Continue)...")
        continue
    
    if fruit == "Orange":
        print("Found Orange, stopping loop (Break)!")
        break
        
    print(f"Eating {fruit}")
