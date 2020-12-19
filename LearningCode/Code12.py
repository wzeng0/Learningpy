# calculates user's input

first_num = input("Please input a number: ")
op = input("Please input operation: ")
second_num = input("Please input another number: ")


def function(num1, operator, num2):
    if operator == "+":
        return(float(num1) + float(num2))
    elif operator == "-":
        return(float(num1) - float(num2))
    elif operator == "*":
        return(float(num1) * float(num2))
    elif operator == "/":
        return(float(num1) / float(num2))
    else:
        return("Invalid operator")

print(function(first_num, op, second_num))