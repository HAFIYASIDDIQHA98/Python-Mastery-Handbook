temp = float(input("Enter temperature: "))
unit = input("Is this (C)elsius or (F)ahrenheit? ").upper()

if unit == "C":
    converted = (temp * 9/5) + 32
    print(f"{temp}°C is {converted:.2f}°F")
elif unit == "F":
    converted = (temp - 32) * 5/9
    print(f"{temp}°F is {converted:.2f}°C")
