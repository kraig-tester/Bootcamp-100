import random
from os import system
from art import logo,vs
from game_data import data

def game():
    game_over = False
    score = 0
    a = None
    b = None

    system("cls")

    while not game_over:
        
        print(logo)

        if a != None and b != None:
            print(f"You're right! Current score: {score}")
        
        options_differ = False
        
        while not options_differ:
            a = random.choice(data)
            b = random.choice(data)

            if a != b:
                options_differ = True

        a_followers = a["follower_count"]
        b_followers = b["follower_count"]
        
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        system("cls")

        if a_followers > b_followers and answer == "a" or b_followers > a_followers and answer == "b":
            score += 1
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True

game()