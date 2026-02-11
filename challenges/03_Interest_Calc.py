def simple_interest():
    p = float(input("Enter Principal amount: "))
    r = float(input("Enter Rate of interest: "))
    t = float(input("Enter Time (years): "))
    
    interest = (p * r * t) / 100
    total = p + interest
    
    print(f"💰 Interest: ${interest}")
    print(f"🏦 Total Amount: ${total}")

simple_interest()
