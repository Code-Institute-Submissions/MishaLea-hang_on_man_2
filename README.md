# Hang on Man

## Purpose
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
-	After a set number of words has been guessed right/wrong, the results showing 
final wins/losses would be interesting to see. 
## Features to include: 
-	Graphics of hangman if user gets a guess wrong during each round. 
-	Computer informs user each time they guess right or wrong. If correct, the letter will be added. 
If wrong, a section of hangman to be shown. 
At end of round, computer will have a congrats message or a condolences messages and a function has been created to iterate a new game
whether win or lose. 

** id like to clarify that even though it's working perfectly fine on github, for some reason it's not working on heroku. 
I have spoken to Tutor support and they have confirmed there is no technical reason why it's not working. 




## Graphics included: 
As previously discussed, a simple hangman design will be added each time a letter is guessed incorrectly – 
this has been added directly into the python code through an if/elif/else statement based on the number of turns taken. 

Each round will show ‘_’ underscores based on how many letters are in the randomly chosen word. When a letter is 
guessed correctly, this will be added in the correct space. 

*IntroScreen
![IntroScreen](/assets/images/IntroScreen.jpg)

The above image shows the command line promting the user to enter a letter with a brief description on 
the game and how many lives they have in total. Followed 

*Correctanswer
![Correctanswer](/assets/images/Correctanswer.jpg)

The above image shows the user when a letter has been guessed correctly. 'Congrats! You got a letter. 
And any guesses remaining show along with the sections of hangman 
also used. 

*IncorrectGuess
![IncorrectGuess](/assets/images/IncorrectGuess.jpg)

If the user gets a letter wrong, the computer informs them with 
'Unlucky, try again!' followed by the number of guesses remaining
and the section of hangman added. 

*Letterguessedalready
![Letterguessedalready](/assets/images/Letterguessedalready.jpg)

If the user guessed a letter that has already been entered on the same round, no lives are lost, 
however the computer will advise them that 'You've already guessed that letter! Try again'

*invalidinput
![invalidinput](/assets/images/invalidinput.jpg)

If a user inputs anything other than a letter from the alphabet, they will be advised 
'Invalid input! Try again' Again. no lives are taken at this stage. 

*roundlost
![roundlost](/assets/images/roundlost.jpg)

If all lives have been used and the word was not guessed, the hangman image will show 
in commpletion along with the message 'Unlucky, try again! Along with the word that was randomly 
generated for that round. 

*WordGuessedCorrectly
![WordGuessedCorrectly](/assets/images/WordGuessedCorrectly.jpg)

When the user guesses the word correctly, it will show the word in full and the message of congratulations! 



Correct input and validation: 
To make sure the user inputs valid characters IE a,b,c,d etc… , the code will include instructions 
if an invalid answer is submitted, advising the user to only use valid letters. This will not affect 
the chances left – only when a valid letter has been submitted wrongly, will the number of guesses decrease.
Similarly, if the user inouts a letter more than once, the computer will generate a message advising the 
letter has already been guessed.  

## Solved errors and bugs/errors unresolved: 

There were several minor errors including whitespaces, extra lines and an error message detailing 
the variable was not entered correctly using UPPERCASE characters. 
All errors were fixed except for in the Gitpod.yml

*Problems
![Problems](/assets/images/Problems.jpg)

I had spoken with tutor support about these errors and was assured this would not affect my project or the app itself. 

PIP8 was used and confirmed all was correct with the code. 
*PEP8Valid
![PEP8Valid](/assets/images/PEP8Valid.jpg)


References/ Acknowledgements:
 
-	https://www.randomlists.com/data/words.json - used to collect a group of random words
-	import random was added to run.py to randomly select from the chosen list of words. 
-	Youtube videos (devjunkie) helped clarify certain sections of the code I was not familiar with. Such as the graphics for the hangman. 


