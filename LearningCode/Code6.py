
# list of lucky numbers
lucky_numbers = [4, 5, 6, 2, 7, 8, 9]

# list of string of friend's name
friends = ["Vincent", "Katie", "Kirthi", "Arthi", "Shirley"]

# extend function appends a list onto an existing list
# changes the existing list by adding on new elements
friends.extend(lucky_numbers)

# appends another item onto the list
friends.append("Happy")

# insert takes two parameters
# parameter one takes an index of where you want to add another element
# parameter two takes an item and puts the item in the place of the given index
friends.insert(3, "Kelly")

# remove takes away the given item from the lsit
friends.remove(2)

# friends.clear() clears the whole list

# pop removes the last element of the list
friends.pop()

# gives the index of the given item
# if item is not in the list, produces an error message
print(friends.index("Katie"))

# counts how many times the given item shows up in the list
friends.insert(5, "Vincent")
print(friends.count("Vincent"))

# sorts the list alphabetically if string and ascending numerical order if number
# if string contains multiple types of data, code will not be able to sort itself
lucky_numbers.sort()

# reverses the items in the list
friends.reverse()

# copies list into another list
friends2 = friends.copy()

print(friends)
print(lucky_numbers)
print(friends2)