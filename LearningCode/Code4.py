# asks user to input their name and age
name = input("Please enter your name: ")
age = input("Please enter your age: ")
# welcomes the user and asks them to choose a class
print("Welcome " + name)
print("Please choose a class: ")

num1 = input("Please enter a number: ")
num2 = input("Please enter another number: ")
# this code will result in a string and not a algebraic equation
# result = num1 + num2
# therefore, use this
# ints produce integer numbers from string
# this however, limits your input to integers in strings
result1 = int(num1) + int(num2)
# in order to be able to use decimals, can use function "float"
result2 = float(num1) + float(num2)
print(result1)
print(result2)