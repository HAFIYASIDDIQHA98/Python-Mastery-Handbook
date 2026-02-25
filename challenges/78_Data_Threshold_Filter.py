sensor_readings = [22.5, 45.0, 10.2, 88.7, 34.1, 95.0]
threshold = 50.0

# Keeping only readings above the threshold
high_readings = [val for val in sensor_readings if val > threshold]

print(f"All Readings: {sensor_readings}")
print(f"Alert Readings (>50): {high_readings}")
