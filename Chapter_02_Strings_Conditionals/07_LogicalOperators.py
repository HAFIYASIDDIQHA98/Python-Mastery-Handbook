# Using AND / OR
is_student = True
has_id = False

if is_student and has_id:
    print("Entry Allowed (Both conditions met)")
elif is_student or has_id:
    print("Partial Entry (One condition met)")
else:
    print("Access Denied")
