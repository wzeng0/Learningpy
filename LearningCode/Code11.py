
# function finds the greatest number between the given 3 numbers
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: # checks first number to check if greatest
        return(num1)
    # num 2 only checks if it is greater than num 3 because
    # num 2 already checks if num 1 is greater than num 2
    elif num2 >= num3:
        return(num2)
    # if all test fails, then num3 will definitely be larger than the other 2
    else:
        return(num3)

print(max_num(4, 5, 2))
print(max_num(3, 2, 1))
print(max_num(1, 2, 3))


# stores user's gender as a variable
gender = input("What is your gender?: ")
# system returns the string given user's gender
# if user is a male, system will repeat if male
# if not, system will tell user that it is not a male
def find_gender(genders):
    if genders == "male": # double equal sign checks if two values are equal
        return("You are a male")
    else:
        return("You are not a male")

# test case
print(find_gender(gender))

# not equal to
3 != 2