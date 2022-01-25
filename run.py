# setup the word and hidden list
import random
def hang_on_man():
    words = ['tree', 'sun', 'ball', 'moon', 'earth', 'grass', 'world',
            'advert', 'octodont', 'pharos', 'physics', 'reality',
            'possession', 'cousin', 'aspect', 'analyst']


    # user input
    user_input = input('Welcome to Hang on, Man. To continue. enter name: ')
    print(user_input)

    """
    user_rules provides the option to either: a) read rules before the game 
    or continue straight to game.
    """
    user_rules = input("For Rules, press 'Y' otherwise, press 'C' to continue. ")
    print(user_rules)

    if user_rules == 'Y':
        print("You have 10 chances to get the word right.") 
        print("For a hint, 1 life will be deducted from lives remaining")
        print("Keep track of how many lives left with the hangman image")
        print("Have fun and Hang on, Man!")
    else:
        user_rules == 'C'
        print("Ok, let's play! Good luck!")

    
    user_guess = 


hang_on_man()

"""
# loop until either the player has won or lost
def valid_word(words):
    word = random.choice(words)
    while '_' in word:
        word = random.choice(words)

    return word


# display the current boards, guessed letters, and attempts remaining
def hang_on_man():
    word = valid_word(words)
    words_letters = set(words)
    alphabet = set(words)
    used_letters = set()

    lives = 10

    # user input
    while len(words_letters) > 0:
        # need 2 things - letters already used
        print('You have already used these letters.' ' '.join(used_letters))
        
        # tell user wjat current word is
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', '' .join(word_list))

        user_letter = input('Guess a letter')
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in words_letters:
                words_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You already used that letter, try again!')

        else:
            print('Invalid character. Try again.')


# while len of words_letters == 0, iterate.
hang_on_man()


user_input = input('Welcome to Hang on, Man. To continue. enter name.')
print(user_input)


# ask the player for a character

# if the player guessed correct. show all matched letters and print message

# if the player guessed wrong, print failure message and increment attempts

# if the player has won, print the a win message and stop looping

# if the player has lost, print falling and stop looping
"""