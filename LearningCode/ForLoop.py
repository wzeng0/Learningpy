
# for loop for a string prints out individual element in string
for letter in "Hello Word":
    print(letter)

# for loops for list prints out every item of the list
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

# for loop for range prints out number within the range excluding the last number
for index in range(10):
    print(index)
# prints out number starting from 3 ending at 9
for index in range(3, 10):
    print(index)

# prints every item in list friends
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")