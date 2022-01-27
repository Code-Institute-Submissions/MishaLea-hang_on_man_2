"""
    Random library imported for word choosing random
    word from below list by random.
"""
import random

WORDBANK = ['tree', 'sun', 'ball', 'moon', 'earth', 'grass', 'world',
            'advert', 'octodont', 'pharos', 'physics', 'reality',
            'possession', 'cousin', 'aspect', 'analyst']


class Hangman:
    """
        Class used to create the objects that are included in the below
        variables and functions.
    """
    word = ""
    incorrect_guesses = 0
    guessed_letters = []

    username = input("Enter your name to start: ")
    print("Username is: " + username)

    def start_game(self):
        """
            Method to start the game.
        """
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Hang on, Man!\n")
        print("Guess letters to fill out the word--you have 6 attempts!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()

        self.word = random.choice(WORDBANK)

        while True:
            # Check if the game has already been lost
            if self.incorrect_guesses == 6:
                print(f"You DIE! The word was '{self.word}' :(")
                break

            # Check if the game has already been won
            did_win = True
            for letter in self.word:
                if letter not in self.guessed_letters:
                    did_win = False
                    break
            if did_win:
                # The player has won the game!
                self.display_game_board()
                print("Well done, you've guessed the word!")
                break

            # Display board and play the game
            self.display_hangman()
            self.display_game_board()
            self.prompt_user()

    def display_hangman(self):
        """
        Method to display the hanging man representing wrong guesses.
        """
        print()
        print()
        if self.incorrect_guesses == 0:
            print("6 guesses allowed")
            print("-----------------")
            return
        elif self.incorrect_guesses == 1:
            print("5 guesses left")
            print("-----------------")
            print("         0       ")
        elif self.incorrect_guesses == 2:
            print("4 guesses left")
            print("-----------------")
            print("         0       ")
            print("         |       ")
        elif self.incorrect_guesses == 3:
            print("3 guesses left")
            print("-----------------")
            print("         0       ")
            print("         |       ")
            print("        / \\      ")
        elif self.incorrect_guesses == 4:
            print("2 guesses left")
            print("-----------------")
            print("       \\ 0 /     ")
            print("         |       ")
            print("        / \\      ")
        elif self.incorrect_guesses == 5:
            print("Only 1 guess left!")
            print("-----------------")
            print("         |       ")
            print("       \\ 0 /     ")
            print("         |       ")
            print("        / \\      ")
        else:
            print("------------------")
            print("        _|_      ")
            print("         |       ")
            print("       \\ 0 /     ")
            print("         |       ")
            print("        / \\      ")
        print()
        print()

    def display_game_board(self):
        """
        Method to display blank spaces and guessed letters.
        """
        # Build the current guessed word
        game_board = ""
        for character in self.word:
            if character in self.guessed_letters:
                game_board += " " + character + " "
            else:
                game_board += " _ "
        print()
        print(game_board)
        print()

    def prompt_user(self):
        # Ask the user to guess a letter
        """
        Method to prompt the user to guess a letter, and process the input.
        """
        letter = input('Guess a letter: ')

        if len(letter) > 1 or (not letter.isalpha()):
            print("Invalid input! Try again.")
            return

        # Already guessed letters are invalid
        if letter in self.guessed_letters:
            print("You've already guessed that letter! Try again.")
            return

        # Add the current guess to the list of guessed letters
        self.guessed_letters += letter

        # Check if this is a correct letter
        if letter in self.word:
            print("Congrats! You got a letter.")
        # If this is not a correct guess, increment incorrect guesses
        else:
            self.incorrect_guesses += 1
            print("Unlucky, try again!")


Hangman().start_game()
