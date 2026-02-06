
def recursive_sum(n):
    if n <= 1:
        return n
    else:
        return n + recursive_sum(n - 1)

num = int(input("Enter a limit: "))
print(f"The sum of first {num} numbers is: {recursive_sum(num)}")
