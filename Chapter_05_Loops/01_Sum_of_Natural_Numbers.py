# Sum of first N natural numbers using a while loop
n = int(input("Enter the value of N: "))
sum_total = 0
i = 1

while i <= n:
    sum_total += i
    i += 1

print(f"The sum of first {n} numbers is: {sum_total}")
