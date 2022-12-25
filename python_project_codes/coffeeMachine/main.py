MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def print_report(command):
    """Take command as input and prints report"""
    if command == 'report':
        for item in resources:
            print(f"{item}: {resources[item]}")
        print(f"money: {money}")
        take_order()


def check_resources(drink):
    """Take drink as input and returns available or insufficient_resource"""
    for item in resources:
        if MENU[drink]['ingredients'][item] < resources[item]:
            return 'available'
        else:
            return item


def adjust_resources(drink):
    """adjusts resources taken by drink"""
    for item in resources:
        resources[item] -= MENU[drink]['ingredients'][item]


def take_order():
    global money
    command = input("What would you like? (espresso/latte/cappuccino):")
    if command == 'off':
        exit("off")

    if command in MENU:
        drink = command
        if check_resources(drink) == 'available':
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            coin_value = quarters * 0.25 + dimes * .1 + nickels * .05 + pennies * .01
            price = MENU[drink]['cost']
            change = round((coin_value - price), 2)

            if change >= 0:
                if change > 0:
                    print(f"Here is ${change} in change.")
                print(f"Here is your {drink}, Enjoy!")
                adjust_resources(drink)
                money += price
            else:
                print("Insufficient money entered!. Money refunded.")
                take_order()

        else:
            print(f"Sorry there is not enough {check_resources(drink)}")
            take_order()
    else:
        print_report(command)
        take_order()


while True:
    take_order()