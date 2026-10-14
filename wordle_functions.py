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

def choose_word():
    global unused_words
    global used_words
    if len(unused_words) == 0:
        unused_words.extend(used_words)
        used_words.clear()
    word = rd.choice(unused_words)
    unused_words.remove(word)
    used_words.append(word)
    return word

def get_guess():
    while True:
        try:
            guess = input("Enter a guess: ")
            guess_length = len(guess)
            if guess_length != 5:
                print("Please guess a 5 letter word. ")
        except:
            print("Something went wrong, please try again.")
        break
    return guess.lower()

def evaluate_guess(secret_word, player_guess):
    secret_word_list = []
    player_guess_list = []
    result = []
    for i in range(5):
        if player_guess[i] != secret_word[i]:
            result.append


def display_guess(player_guess):
    print(" ".join(player_guess.uppper()))

def has_won():

