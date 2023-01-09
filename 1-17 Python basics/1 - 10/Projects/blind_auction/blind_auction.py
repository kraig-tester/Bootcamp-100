from os import system, name
from art import logo

def clear():
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')


bids = {}
running = True

print(logo)

while running:
    new_key = input("What is your name?: ")
    new_value = int(input("What is your bid?: $"))
    bids[new_key] = new_value

    more_bids = input("Are there any other bidders? Type 'Yes' or 'No'. ").lower()
    if more_bids == "yes":
        clear()
    else:
        clear()
        running = False

bidder = ""
highest_bid = 0

for key in bids:
    bid_amount = bids[key]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        bidder = key

print(f"The winner is {bidder} with a bid of ${highest_bid}.")