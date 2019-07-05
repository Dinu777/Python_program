# Q1. Write a program that uses input() to prompt a user for their name and then welcomes them.
# Example Output:
# Enter your name: Rama
# Hello Rama

# name = input("what is your name ?  ")
# print(name)

name = input("what is your name ?  ")

while not name.isalpha():
    print('that\'s not a name.......')
    name = input("Enter a valid name :")

print("Hello " + name)
