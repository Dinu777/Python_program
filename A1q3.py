# Q3. Write a program to prompt the user for hours and rate per hour to compute gross pay. Your pay computation
# should be to give the employee 1.5 times the hourly rate for hours worked above 40 hours. (Both 'hours' and 'Rate'
# are inputs from the user)
# Example Output:
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
#
# Enter Hours: 30
# Enter Rate: 5
# Pay: 150

hour = int(input("Enter Hours : "))
rate = int(input("Enter Rate : "))

if hour < 40:
    print("Pay : " + str(hour * rate))
else:
    print("Pay : " + str(40 * rate + 1.5 * rate * (hour - 40)))
