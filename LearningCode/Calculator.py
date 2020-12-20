# making a calculator that returns a value based on the user's inputs

num1 = input("Enter a value: ")
op = input("Enter an operation: ")
num2 = input("Enter another value: ")

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

print(calculate(num1, op, num2))