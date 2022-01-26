"""
Randomm library imported for word choosing random
word from below list by random.
"""
import random

words = ['tree', 'sun', 'ball', 'moon', 'earth', 'grass', 'world',
         'advert', 'octodont', 'pharos', 'physics', 'reality',
         'possession', 'cousin', 'aspect', 'analyst']

word = random.choice(words)

incorrectGuesses = 0
guessedLetters = []

print("Hang on, Man!")
print("Choose a letter to start - You have 6 attempts")

while True:
    # Build the current guessed word
    currentGuessedWord = ""
    for character in word:
        if character in guessedLetters:
            currentGuessedWord += character
        else:
            currentGuessedWord += " _ "
    print()
    print(currentGuessedWord)
    print()

    # Check if the user has already guessed all the letters
    if currentGuessedWord == word:
        print("Well done, you've guessed the word!")

    # Check if the player has lost the game
    if incorrectGuesses == 1:
        print("5 turns left")
        print("-----------------")
        print("         0       ")
    if incorrectGuesses == 2:
        print("4 turns left")
        print("-----------------")
        print("         0       ")
        print("         |       ")
    if incorrectGuesses == 3:
        print("3 turns left")
        print("-----------------")
        print("         0       ")
        print("         |       ")
        print("        / \      ")
    if incorrectGuesses == 4:
        print("2 turns left")
        print("-----------------")
        print("       \ 0 /     ")
        print("         |       ")
        print("        / \      ")
    if incorrectGuesses == 5:
        print("Only 1 turn left!")
        print("-----------------")
        print("         |       ")
        print("       \ 0 /     ")
        print("         |       ")
        print("        / \      ")
    if incorrectGuesses == 6:
        print(f"You DIE! The word was {word} :D")
        print("-----------------")
        print("        _|_      ")
        print("         |       ")
        print("       \ 0 /     ")
        print("         |       ")
        print("        / \      ")
        break

    # Ask the user to guess a letter
    letter = input('Guess a letter: ')

    # Already guessed letters are invalid
    if letter in guessedLetters:
        print("You've already guessed that letter! Try again.")
        continue

    # Add the current guess to the list of guessed letters
    guessedLetters += letter

    # Check if this is a correct letter
    if letter in word:
        print("Congrats! You got a letter.")
    # If this is not a correct guess, increment incorrect guesses
    else:
        print("Unlucky, try again!")
        incorrectGuesses += 1
