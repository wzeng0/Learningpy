# prints a string with \n which puts the rest of the string on another line
print("Hello\nWorld")
# escape character means inputting a key literally
# \" means literal quotation marks instead of ending string
print("As someone once said \"When the going gets tough, the tough get going!\"")

# storing a string inside a variable
phrase = "Hello World"

# concatenation in variable
print(phrase + " Code")

# cool functions with printing a variable
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper()) # checks if the whole string is uppercase and returns a boolean
print(phrase.upper().isupper())
print(len(phrase)) # finds how many characters are inside the string (space counts)
print(phrase[0]) # finds the character at the given index of the string
print(phrase[5])
print(phrase.index("o")) # calling a value is called passing a parameter
print(phrase.index("H"))
# print(phrase.index("h")) is not part of the string because it is lowercase so will return error
print(phrase.index("World")) # gives the index of where the word starts in the string
print(phrase.replace("World", "Player")) # replaces an item inside the string with the item entered
