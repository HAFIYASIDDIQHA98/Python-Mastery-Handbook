def convert_temp(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Test
c = 37
print(f"{c}°C is equal to {convert_temp(c)}°F")
