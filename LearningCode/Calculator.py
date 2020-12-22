# making a calculator that returns a value based on the user's inputs

def calculate(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    elif op == "=":
        return num1 == num2
    elif op == ">":
        return num1 > num2
    elif op == "<":
        return num1 < num2
    else:
        return op + " is not an operator"
# can catch invalid inputs using try and except
try:
    num1 = float(input("Enter a value: "))
    op = input("Enter an operation: ")
    num2 = float(input("Enter another value: "))
    print(calculate(num1, op, num2))

# normal except would be too simple and bad practice in python

# catches the zero division error
except ZeroDivisionError as err:
    print(err)

# catches the invalid value error
except ValueError as error:
    # print("Invalid Input. Try again.")
    print(error)