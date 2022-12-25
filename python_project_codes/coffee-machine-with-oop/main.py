from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
drink = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    command = input(f"What do you like? {menu.get_items()} ")
    if command == 'off':
        is_on = False
    elif command == 'report':
        drink.report()
        money_machine.report()
    else:
        drink_name = menu.find_drink(command)
        cost_of_drink = drink_name.cost
        if drink.is_resource_sufficient(drink_name) and money_machine.make_payment(cost_of_drink):
            drink.make_coffee(drink_name)

