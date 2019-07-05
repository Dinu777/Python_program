# Q2. Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit,
# and print out the converted temperature. (Use your own ideas for user prompt statements, and output print)
# (0°C × 9/5) + 32 = 32°F

celsius = input("Enter temperature in Celsius : ")

while not celsius.isnumeric():
    print('that\'s not a temperature.......')
    celsius = input("Enter a valid temperature in Celsius : ")
else:
    fahrenheit = (int(celsius) * 9 / 5) + 32
    print("the Fahrenheit conversion of " + str(celsius) + " is " + str(fahrenheit))





