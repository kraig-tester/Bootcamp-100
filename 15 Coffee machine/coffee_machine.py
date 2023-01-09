from coffee_data import MENU, resources


def replenish_resources():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100

    print("Resources has been replenished!")


def print_report(money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${str('{:0.2f}'.format(money))}")


def proceed_order(order, money):
    menu_item = MENU[order]

    sufficient_resources = True
    for item in menu_item["ingredients"]:
        if resources[item] < menu_item["ingredients"][item]:
            print(f"Sorry there is not enough {item}")
            sufficient_resources = False

    if sufficient_resources:
        print(f"Price for {order} is {'{:0.2f}'.format(menu_item['cost'])}. Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        total_money = quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01

        if total_money < menu_item['cost']:
            print("Sorry that's not enough money. Money refunded.")
        else:
            change = total_money - menu_item['cost']
            if change != 0:
                print(f"Here is ${str('{:0.2f}'.format(change))}")

            for item in menu_item["ingredients"]:
                resources[item] = resources[item] - menu_item["ingredients"][item]
            
            money += menu_item['cost']
            print(f"Here is your {order}. Enjoy!")    
        return money


def main():
    money_in_machine = 0
    running = True
    while running:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if order == "report":
            print_report(money_in_machine)    
        elif order in MENU:
            money_in_machine = proceed_order(order, money_in_machine)
        elif order == "quit" or order == "exit":
            print("Thank you for using our 'Coffee Machine'")
            running = False
        elif order == "replenish":
            replenish_resources()
        else:
            print("Invalid input, try again.")
        
    return


main()
    