*Hang on Man*

# Purpose
Hang on, Man Is a command line game based on the original HangMan letter game.
The computer will generate a random set of words and the user has to guess the 
correct word/letters with a limited amount of tries for each word. 
 
The game itself will have a set of words pre-installed that will generate one 
randomly for the user to guess correctly with the allotted amount of tries for each word. 

They will be random words, with no theme or genre.
Each word will have a maximum of 6 attempts to get the word right and for sake of
difficulty, will include longer words in my set of random words that will be generated 
on each round. If the user gets it right, he/she wins that round. If the user loses, 
it will inform the user they lost the round. 

## Initial concept/Ideas: 
The UI will be simple but for each round, a piece/section of graphic will be added 
depending on the guess being wrong. This will signal to the user their chances are 
nearing the end if they guess more wrong answers. If they are lucky and manage to 
guess the letters/word before their turn is up, the hangman will not be completed. 
***I would like to include a basic graphic design if the player wins the round - 
I am yet to create this so still in concept stage currently.  

## User Stories

As a User
-	The game needs to be easy to understand and fun to play. 

To create this I intend on keeping content/words brief
. 
-	The rules need to be clear with the number of tries showing after each letter is guessed. 
-	An option to play again after each word is guessed right/wrong
-	After a set number of words has been guessed right/wrong, the results showing 
final wins/losses would be interesting to see. 
## Features to include: 
-	Graphics of hangman if user gets a guess wrong during each round. 
-	Hint if down to 4/5 attempts that’s only available by swapping a life for a hint. 
-	Computer informs user each time they guess right or wrong. If correct, the letter will be added. 
If wrong, a section of hangman to be shown. 
-	User should enter name to start and before initial guess, computer will welcome the user to the game. 
At end of round, computer will have a congrats message or a condolences messages with an option to play again. 

Graphics included: 
As previously discussed, a simple hangman design will be added each time a letter is guessed incorrectly – 
this has been added directly into the python code through an if/else statement based on the number of turns taken. 

Each round will show ‘_’ underscores based on how many letters are in the randomly chosen word. When a letter is 
guessed correctly, this will be added in the correct space.  


Correct input and validation: 
To make sure the user inputs valid characters IE a,b,c,d etc… , the code will include instructions 
if an invalid answer is submitted, advising the user to only use valid letters. This will not affect 
the chances left – only when a valid letter has been submitted wrongly, will the number of guesses decrease.
Similarly, if the user inouts a letter more than once, the computer will generate a message advising the 
letter has already been guessed.  

Solved errors and bugs/errors unresolved: 

There were several minor errors including whitespaces, extra lines and an error message detailing 
the variable was not entered correctly using UPPERCASE characters. 
All errors were fixed except for in the Gitpod.yml
(image)
I had spoken with tutpr support about these errors and was assured this would not affect my project or the app itself. 

PIP8 was used and confirmed all was correct with the code. 
(image) 



References/ Acknowledgements:
 
-	https://www.randomlists.com/data/words.json - used to collect a group of random words
-	import random was added to run.py to randomly select from the chosen list of words. 
-	Youtube videos (devjunkie) helped clarify certain sections of the code I was not familiar with. Such as the graphics for the hangman. 


