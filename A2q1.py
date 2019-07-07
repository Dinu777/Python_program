# Q1. Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered,
# print out the total, count, and average of the numbers. If the user enters anything other than a number,
# detect their mistake using try and except and print an error message and skip to the next number.

# Example Output:
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.33333333333

i = 0
a = list()
a.append(input("Enter a number: "))

while a[i] != "done":
    if not a[i].isnumeric():
        print("Invalid input")
    i += 1
    a.append(input("Enter a number: "))

b = list()

for i in a:
    if i.isnumeric():
        b.append(int(i))

print("\nSum of all the numbers : " + str(sum(b)))
print("Length of array : " + str(len(b)))
print("Average of all the numbers entered : " + str(sum(b)/len(b)))
