from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# Create Objects
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

is_on = True


# Initial Report
coffe_maker.report()
money_machine.report()


# Coffee Machine Loop
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice == "off".lower():
        is_on = False

    elif choice == "report".lower():
        coffe_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)

        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)