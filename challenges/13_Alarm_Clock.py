import time

seconds = int(input("How many seconds to wait? "))
for i in range(seconds, 0, -1):
    print(f"Time left: {i}s")
    time.sleep(1)

print("⏰ WAKE UP!")
