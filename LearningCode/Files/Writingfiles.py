# "a" appends to the filee
college_file = open("FriendsCollege.txt", "a")

# appends the string
# if file is ran again, it will append another of the same string
# string will not be on another line
# college_file.write("Mitchell Leung - Cornell University")
college_file.write("\nMitchell Leung - Cornell University")


# if you use w, it will override the whole file and make a new file
# college_file = open("FriendsCollege.txt", "w")
# college_file.write("\nMitchell Leung - Cornell University")

# useful for new websites
# college_file = open("College.html", "w")
# college_file.write("<p> This is HTML </p>")


college_file.close()