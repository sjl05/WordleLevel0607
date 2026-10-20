#Sam Lyon 
# IS303 Hilton
#Creates a wordle game

#imports the wordle functions and makes it shorthand
import wordle_functions as wf

#global variable to track what words the user has guessed already
guesses = []

#main code block
print("Welcome to Wordle\n🟩 = the letter is in the right place\n🟨 = the letter is in the word, but not in the right place\n⬜ = the letter is not in the word")
while True:
    secret_word = wf.choose_word()
    while len(guesses) < 6: #This block runs 6 times to give the user 6 guesses
        print(f"Attempt {len(guesses) + 1} of 6")
        guess = wf.get_guess(guesses)
        guesses.append(guess) #add the user guess to the list of guesses
        feedback = wf.evaluate_guess(secret_word, guess)
        wf.display_guess(guess, feedback)
        won = wf.has_won(secret_word, guess)
        if won: #won defaults to false
            print("You got it!")
            break
    if len(guesses) == 6 and not won: #the user may have guessed 6 times incorrectly
        print(f"The word was: {secret_word}\nYou lose") #prints the correct word
    end_game = wf.end_game_or_not()
    if not end_game: #end_game will return a boolean, that means the game will end if it is True and won't end if it is False
        guesses.clear()
        print("Okay, a new word has been chosen") #this really only works to put here
    else:
        break
print("Thanks for playing!") #be nice to the player
