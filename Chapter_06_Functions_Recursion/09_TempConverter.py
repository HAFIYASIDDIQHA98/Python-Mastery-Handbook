
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

c = float(input("Enter temperature in Celsius: "))
f = celsius_to_fahrenheit(c)

print(f"{c}°C is equal to {f}°F")
