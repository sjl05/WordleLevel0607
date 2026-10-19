import wordle_functions as wf

guesses = []

print("Welcome to Wordle\n🟩 = the letter is in the right place\n🟨 = the letter is in the word, but not in the right place\n⬜ = the letter is not in the word")
while True:
    secret_word = wf.choose_word()
    while len(guesses) < 6:
        print(f"Attempt {len(guesses) + 1} of 6")
        guess = wf.get_guess(guesses)
        guesses.append(guess)
        feedback = wf.evaluate_guess(secret_word, guess)
        wf.display_guess(guess, feedback)
        won = wf.has_won(secret_word, guess)
        if won:
            print("You got it!")
            break
    if len(guesses) == 6 and not won:
        print(f"The word was: {secret_word}\nYou lose")
    end_game = wf.end_game_or_not()
    if not end_game:
        guesses.clear()
        print("Okay, a new word has been chosen")
    else:
        break
print("Thanks for playing!")
