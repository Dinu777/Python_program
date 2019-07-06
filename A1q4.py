# Q4. Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by
# printing a message and exiting the program. The following shows two executions of the program:
# Example Output:

# Run 1 -

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Run 2 -

# Enter Hours: forty
# Error, please enter numeric input
i = 1
print("Run " + str(i) + " - ")
hour = input("Enter Hours : ")
rate = input("Enter Rate : ")

while hour.isalpha() or rate.isalpha():
    print("Error, please enter numeric input")
    i += 1
    print("\nRun" + str(i) + " - ")
    hour = input("Enter Hours : ")
    rate = input("Enter Rate : ")

hour = int(hour)
rate = int(rate)
if hour < 40:
    print("Pay : " + str(hour * rate))
else:
    print("Pay : " + str(40 * rate + 1.5 * rate * (hour - 40)))
