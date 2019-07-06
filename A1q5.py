# Q5. Write a program to find the smallest number in the list [45, 708, 86, 102, 3, 321, 444]. (You can create your
# own list with at least 6 numbers.)

a = [45, 708, 86, 102, 3, 321, 444]
# print(min(a))

for i in range(len(a)):
    j = 0
    while j < len(a) - 1:
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
        j += 1

print(a)
print("The smallest number is " + str(a[0]))
