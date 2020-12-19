
is_male = True
is_tall = False

if is_male and is_tall: # check if you are both tall and male
    print("You are a tall male")
elif is_male and not(is_tall): # checks if you are a male but not tall
    print("You are a short male")
elif not(is_male) and (is_tail): # check if you are tall and not a male
    print("You are tall but not a male")
else: # if none of the conditions are satisfied, then you're both not a male nor tall
    print("You are neither male nor tall")