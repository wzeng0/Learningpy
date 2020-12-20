secret_word = "pineapple"
guess = ""
guess_count = 0

# dictionary of the hints needed for the word
hint = {
    1: "Hint 1: It is yellow",
    2: "Hint 2: It is spiky",
    3: "Hint 3: It grows on trees",
    4: "Hint 4: You can eat this",
    5: "Hunt 5: It is hard on the outside",
    6: "Hint 6: It is a fruit"
}

# while the user's input is not the word, it will return a hint
# when all the hints are given, will stop producing hints and user will have to keep guessing
while guess != secret_word:
    guess = input("Enter guess: ")
    guess_count += 1
    if guess == secret_word:
        print("You win! The word is: Pineapple")
    elif guess_count <= 6:
        print(hint.get(guess_count))
    else:
        print("Try again!")