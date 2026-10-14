"""
Level #7 Assignment – Wordle
IS 303 – Hilton
Create a Python word-guessing game inspired by Wordle.
The computer will select a secret five-letter word. The player gets six attempts to guess the word.
Feedback
After each guess, display feedback for every letter:
• G (Green) means the letter is correct and in the correct position.
• Y (Yellow) means the letter appears in the word but is in the wrong position.
• - means the letter does not appear in the word.
For example:
Secret word: PLANT
Guess: CRANE
Feedback: - - G G -
Program Requirements
Your program should:
1. Welcome the player.
2. Select a secret five-letter word.
3. Give the player up to six guesses.
4. Require each guess to contain exactly five letters.
5. Reject guesses that have already been used.
6. Display feedback after every guess.
7. Tell the player when a letter is correct, misplaced, or absent.
8. End the game when the player guesses the word or uses all six attempts.
9. Display the secret word if the player loses.
10. Ask whether the player would like to play again.
Required Functions
Create and use custom functions in wordle_functions.py. Your program should include the
functions:
• choose_word() – Selects and returns a secret word.
• get_guess() – Gets and validates the player’s guess.
• evaluate_guess() – Compares the guess with the secret word and returns feedback.
• display_guess() – Displays the guess and its feedback.
• has_won() – Determines whether the player has guessed the word.
Additional Requirements
• Import your functions from wordle_functions.py into main.py.
• Use a list to store previous guesses.
• Use meaningful variable and function names.
• Include comments explaining important sections.
• Do not use classes or advanced Python features we have not discussed.
NOTE: For the basic version, you may use secret words that do not contain repeated letters.
Handling repeated letters correctly is an optional challenge.
Sample Session
Welcome to Mystery Wordle!
Guess the five-letter word.
G = correct letter and position
Y = correct letter, wrong position
- = letter is not in the word
Attempt 1 of 6
Enter a five-letter word: crane
Guess: C R A N E
Feedback: - - G G -
Attempt 2 of 6
Enter a five-letter word: slate
Guess: S L A T E
Feedback: - G G - -
Attempt 3 of 6
Enter a five-letter word: plant
Guess: P L A N T
Feedback: G G G G G
Congratulations! You solved the puzzle.
Would you like to play again? no
Thanks for playing!
Submission
Submit a PUBLIC GitHub link containing both files.
"""
import wordle_functions as wf

guesses = []
