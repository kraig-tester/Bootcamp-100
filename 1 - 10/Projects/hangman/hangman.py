import random
from hangman_words import word_list
from hangman_art import logo, stages  

#Preparing variables
hangman_stages = stages

target_word = random.choice(word_list)
target_word_len = len(target_word)
display_word = []
used_letters = []
blank = "_"

letterFound = False
running = True
isWinning = False
attempts = 6

for i in range(target_word_len):
    display_word.append(blank)

#Main
print(f"{logo}\n\n{' '.join(display_word)}\n")

while running:

    guessed_letter = input("Guess a letter: ").lower()

    #Checking for already used letters
    if guessed_letter in used_letters:
        print("Letter has already been used!\nTry another one.")
        print(f"{' '.join(display_word)}\n{hangman_stages[attempts]}")
        continue
    else:
        used_letters.append(guessed_letter)

    #Checking if letter in target word
    for i in range(target_word_len):
        if target_word[i] == guessed_letter:
            display_word[i] = target_word[i]
            letterFound = True

    #Check for winning
    if blank not in display_word:
        isWinning = True
        running = False
        continue

    #Checking for miss    
    if not letterFound:
        print(f"{guessed_letter.upper()} is not in the word!")
        attempts -= 1
        if attempts <= 0:
            running = False
    else:
        letterFound = False
    
    print(f"{' '.join(display_word)}\n{hangman_stages[attempts]}")
        
if isWinning:
    print("\nYou won!")
else:
    print(f"\nYou lost.\nThe word was {target_word}.")
