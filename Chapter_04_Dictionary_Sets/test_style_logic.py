# ==========================================
# CHAPTER 04: DICTIONARY & SETS (MOCK TEST)
# ==========================================

# TEST PROBLEM: Ek dictionary di gayi hai 'inventory', 
# usme se 'price' check karke return karna hai.

# --- YEH SECTION UNKA HOTA HAI (DO NOT TOUCH) ---
def get_product_price(inventory, item_name):
    
    # --- YAHAN AAPKO LIKHNA THA (Inside the function) ---
    # Logic: Check if item exists, then return price
    if item_name in inventory:
        return inventory[item_name]
    else:
        return "Product Not Found."
    # --------------------------------------------------

# --- YEH SECTION BHI UNKA HOTA HAI (INPUT/OUTPUT) ---
if __name__ == '__main__':
    # Sample Data
    store_data = {"Laptop": 50000, "Mouse": 500, "Monitor": 7000}
    
    # Function Call
    result = get_product_price(store_data, "Laptop")
    print(f"Test Result: {result}")
