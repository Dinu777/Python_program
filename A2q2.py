# Q2. Rewrite your pay computation (Assg 1 Q3) with time-and-a-half for overtime and create a function called
# 'computepay' which takes two parameters (hours and rate).

# Example Output:
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0


def computepay(h, r):
    if h < 40:
        print("Pay : " + str(h * r))
    else:
        print("Pay : " + str(40 * r + 1.5 * r * (h - 40)))


hour = input("Enter Hours : ")
rate = input("Enter Rate : ")

while not hour.isnumeric() or not rate.isnumeric():
    print("Error, please enter numeric input")
    hour = input("Enter Hours : ")
    rate = input("Enter Rate : ")

computepay(int(hour), int(rate))
