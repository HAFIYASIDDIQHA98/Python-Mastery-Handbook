def calculate_bmi():
    weight = float(input("Weight in kg: "))
    height = float(input("Height in meters: "))
    
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")
    
    if bmi < 18.5: print("Underweight")
    elif 18.5 <= bmi < 25: print("Normal weight")
    else: print("Overweight")

calculate_bmi()
