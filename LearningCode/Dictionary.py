# given the prefix of the month, returns the name of the full month

# Dictionary values cannot be duplicated
# key : value
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# gives the value associated with the key
print(monthConversions["Nov"])
print(monthConversions.get("Dec"))

# if a key that is not in the dictionary is entered, then it will return none
# if key is not ffound, will return the string given after the comma
# without the get, an error message will appear if key is not in dictionary
print(monthConversions.get("Non", "Not a valid key"))