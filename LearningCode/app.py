# means that you only want to read the file
college_file = open("FriendsCollege.txt", "r")

# means that you want to change the file, writing new and exchanging new info
# open("FriendsCollege.txt", "w")

# mean that you can append new things to the file but you cannot change existing info
# open("FriendsCollege.txt", "a")

# gives all powers of reading and writing
# open("FriendsCollege.txt", "r+")

# before anything, make sure that you can read the file
print(college_file.readable())

# When opening file, close file at the end
college_file.close()
