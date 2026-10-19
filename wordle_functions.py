"""
• choose_word() – Selects and returns a secret word.
• get_guess() – Gets and validates the player’s guess.
• evaluate_guess() – Compares the guess with the secret word and returns feedback.
• display_guess() – Displays the guess and its feedback.
• has_won() – Determines whether the player has guessed the word.
"""
import random as rd

unused_words = ["apple", "beach", "chair", "dance", "earth", "flame", "grape", "house", "input", "jelly", "knife", "lemon", "magic", "night", "ocean", "piano", "queen", "river", "smile", "tiger", "uncle", "voice", "whale", "youth", "zebra", "bread", "cloud", "dream", "entry", "fresh", "ghost", "honey", "ivory", "juice", "kayak", "laugh", "money", "novel", "olive", "peace", "quick", "radio", "sleep", "table", "unity", "vivid", "woman", "yeast", "charm", "stone"]
used_words = []

def choose_word(): #Selects and returns a secret word.
    global unused_words
    global used_words
    if len(unused_words) == 0:
        unused_words.extend(used_words)
        used_words.clear()
    word = rd.choice(unused_words)
    unused_words.remove(word)
    used_words.append(word)
    return word

def get_guess(previous_guesses): #Gets and validates the player’s guess.
    while True:
        guess = input("Enter a guess: ").strip().lower()
        if len(guess) != 5:
            print("Please guess a 5 letter word. ")
            continue
        elif guess in previous_guesses:
            print("You already tried that, guess again.")
            continue
        else:
            break
    return guess

def evaluate_guess(secret_word, player_guess): #Compares the guess with the secret word and returns feedback.
    result = []
    if secret_word == player_guess:
        result = "🟩🟩🟩🟩🟩"
    else:
        for i in range(5):
            if player_guess[i] != secret_word[i] and player_guess[i] in secret_word:
                result.append("🟨")
            elif player_guess[i] != secret_word[i]:
                result.append("⬜")
            elif player_guess[i] == secret_word[i]:
                result.append("🟩")
        result = "".join(result)
    return result

def display_guess(player_guess, feedback): #Displays the guess and its feedback.
    guess = " ".join(player_guess.upper())
    print(f"Guess:    {guess}")
    print(f"Feedback: {feedback}")

def has_won(secret_word, player_guess): #Determines whether the player has guessed the word.
    win = False
    if secret_word == player_guess:
        win = True
    return win

def end_game_or_not():
    """Returns False by default"""
    end_game = False
    while True:
        play_again = input("Do you want to play again? ")
        if play_again == "Yes" or play_again == "yes":
            break
        elif play_again == "No" or play_again == "no":
            end_game = True
            break
        else:
            print("Please type [yes] or [no]")
    return end_game
            