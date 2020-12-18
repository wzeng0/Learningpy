
# one can make a list using []
# one can make a list with all 3 types of data; boolean, number, string
friends = ["Kevin", "Karen", "Jim"]

print(friends)

# prints the first item of the given list
print(friends[0])

# prints the last item of the given list
print(friends[-1])

# prints the elements of the list from index position 1 to the end
print(friends[1:])

# tests for different index
# does not grab the element in the second index
print(friends[1:2]) # does not print element from index 2
print(friends[1:3]) # does not print element from index 3
print(friends[-3:-1]) # does not reverse the output value

# prints the item in the list of the given index
# reports an error when inputed integer is out of bounds
# the given number must be an integer number
index = int(input("Please input a number: "))
print(friends[index])