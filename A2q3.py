# Q3. Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence: 0.8475'
# Use find and string slicing to extract the portion of the string after the colon character and
# then use the float function to convert the extracted string into a floating point number and
# print the floating point number.

a = "X-DSPAM-Confidence: 0.8475"
b = float(a[20:])
print(b)

