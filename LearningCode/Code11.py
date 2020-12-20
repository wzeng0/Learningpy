# finds the maximum number between the given 3

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2>=num3:
        return num2
    else:
        return num3

print(max_num(3, 2, 1))
print(max_num(3, 6, 2))
print(max_num(5, 3, 9))

# to find =, use == to see if string, number, or boolean is equal to another