# Task 72: Filtering based on conditions
# Example: Identifying active users (True = Active, False = Inactive)
user_status = [True, False, True, True, False]
users = ["User1", "User2", "User3", "User4", "User5"]

# Filtering only active users
active_users = [users[i] for i in range(len(users)) if user_status[i] == True]

print(f"Total Users: {users}")
print(f"Active Users Only: {active_users}")
