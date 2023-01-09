from art import logo
from os import system
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(hand):
    hand.append(random.choice(cards))
    
def calculate_score(hand):
    score = sum(hand)
    if score == 21:
        score = 0
    elif score > 21:
        for card in range(len(hand)):
            if hand[card] == 11:
                hand[card] = 1
                score = sum(hand)

    return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer has black jack! You lose!"
    elif user_score == 0:
        return"You have black jack! You win!"
    elif user_score > 21:
        return "You went over! You lose!"
    elif computer_score > 21:
        return "Computer went over! You lose!"
    elif user_score > computer_score:
        return"You scored more! You win!"
    else:
        return "Computer scored more! You lose!"

def play_blackjack():
        
    system('cls')

    game_ended = False
    user_cards = []
    computer_cards = []
    
    print(logo)  

    for number in range(2):
        deal_card(user_cards)
        deal_card(computer_cards)
    
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"    Your cards:{user_cards}, current score: {user_score}")
    print(f"    Computer's first card: {computer_cards[0]}")

    while not game_ended:
        continue_answer = input("Type 'y' to get another card, type 'n' to pass:")
        if continue_answer == "y":
            deal_card(user_cards)
            user_score = calculate_score(user_cards)

            print(f"    Your cards:{user_cards}, current score: {user_score}")
            print(f"    Computer's first card: {computer_cards[0]}")
            
            if user_score > 21 or user_score == 0:
                game_ended = True
        else:
            game_ended = True

    while computer_score != 0 and computer_score < 17:
        deal_card(computer_cards)
        computer_score = calculate_score(computer_cards)


    print(f"    Your final cards:{user_cards}, final score: {user_score}")
    print(f"    Computer's final cards: {computer_cards}, final score: {computer_score}")

    print(compare(user_score, computer_score))


running = True

while running:
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if answer == "y":
        play_blackjack()   
    elif answer == "n":
        running = False
    else:
        print("Invalid input, try again...")