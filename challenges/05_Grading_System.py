def calculate_grade():
    score = float(input("Enter student score (0-100): "))
    
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 35:
        grade = "D (Pass)"
    else:
        grade = "F (Fail)"
        
    print(f"Student Result: {grade}")

calculate_grade()
