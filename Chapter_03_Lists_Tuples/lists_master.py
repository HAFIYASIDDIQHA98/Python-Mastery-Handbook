# ==========================================
# CHAPTER 03: LISTS & TUPLES (HACKERRANK STYLE)
# ==========================================

# Problem: Ek function likho jo list ke numbers ka square return kare
# HackerRank style mein aise likhte hain:

def get_squares(numbers):
    # Step 1: Logic likho (Inside the function)
    result = [x**2 for x in numbers]
    
    # Step 2: Return karo (Zaroori hai!)
    return result

# --- Testing the logic (HackerRank provides this part in-built) ---
my_list = [2, 4, 6]
final_output = get_squares(my_list)
print(f"Squares: {final_output}")


# --- IMPORTANT TIP FOR HACKERRANK ---
# Agar function 'return' mang raha hai, toh 'print' karne se test pass nahi hoga.
# Hamesha result ko RETURN karein.
