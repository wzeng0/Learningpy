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

# reads all the lines of the text file
# print(college_file.read())

# reads the first line of the text file
# if printed multiple times, it will go down the files lines
# first prince prints first line
# second print prints second line... etc.
# print(college_file.readline())

# takes all the lines of the file and turns it into a list
# print(college_file.readlines())

# cannot read lines multiple times so had to comment the top one out
# will read the first item of the list
# print(college_file.readlines()[0])

# to go through all the items in the list,
for friend in college_file.readlines():
    print(friend)

# When opening file, close file at the end
college_file.close()
