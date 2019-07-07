# Q1.Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the
# numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list
# and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.
# Example Output:
# Enter a number: 6
# Enter a number: 2
# Enter a number: 9
# Enter a number: 3
# Enter a number: 5
# Enter a number: done
# Maximum: 9.0
# Minimum: 2.0

i = 0
a = list()
a.append(input("Enter a number: "))

while a[i] != "done":
    i += 1
    a.append(input("Enter a number: "))

a = a[:len(a)-1]
print("Maximum: " + str(max(a)))
print("Minimum: " + str(min(a)))
