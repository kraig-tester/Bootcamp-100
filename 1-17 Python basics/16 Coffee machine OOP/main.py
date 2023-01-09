from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
running = True

while running:
    order = input(f"What would you like? ({menu.get_items()}): ").lower()

    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "exit" or order == "off":
        running = False
    else:
        item = menu.find_drink(order)
        if item != None and coffee_maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)
    