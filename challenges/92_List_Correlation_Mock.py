list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

# Checking if both lists are increasing
if all(list1[i] < list1[i+1] for i in range(len(list1)-1)) and \
   all(list2[i] < list2[i+1] for i in range(len(list2)-1)):
    print("Positive Trend: Both lists are moving upwards.")
