from random import randint
from os import system

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def check_answer(guess, answer):
    if guess == answer:
        return True
    elif guess > answer:
        print("Too high.\nGuess again.")
    else:
        print("Too low.\nGuess again.")
    
    return False
def set_difficulty():
    diff_given = False
    while not diff_given:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == 'hard':
            attempts = 5
            diff_given = True
        elif difficulty == 'easy':
            attempts = 10
            diff_given = True
        else:
            print("Invalid input! Try again.")

    return attempts

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    number = randint(1,100)
    attempts = set_difficulty()
    player_won = False

    while attempts > 0 and not player_won:
        print(f"You have {attempts} attempts remaining to guess the number")
        g_number = int(input("Make a guess: "))

        is_right = check_answer(g_number, number)
        if is_right:
            player_won = True
        else:
            attempts -= 1

    if player_won:
        print(f"You got it! The answer was {number}.")
    else:
        print(f"You lost! The answer was {number}.")

game()