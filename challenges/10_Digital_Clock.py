import time

def digital_clock():
    print("Digital Clock started... (Press Ctrl+C to stop)")
    try:
        while True:
            current_time = time.strftime("%H:%M:%S")
            print(f"\rCurrent Time: {current_time}", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped.")

digital_clock()
