# To convert user input data into Py-Latin
# eg-
# input: Python
# output: ythonpay      [ ython + p + ay ]

original = input("Enter a word : ")

# if len(original) > 0 and original.isalpha():
#     word = original.lower()
#     word = word + word[0] + "ay"
#     word = word[1:len(word)]
#     print("New word : " + word)
# else:
#     print("Invalid input")


while len(original) <= 0 or not original.isalpha():
    print("Invalid Input")
    original = input("Enter a word : ")

word = original.lower()
word = word + word[0] + "ay"
word = word[1:len(word)]
print("New word : " + word)
