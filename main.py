MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
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

COINS = {
    "QUARTER": 0.25,
    "DIME": 0.10,
    "NICKEL": 0.05,
    "PENNY": 0.01,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def process_drink(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        resources[ingredient] -= amount
    resources["money"] += MENU[drink]["cost"]

def add_resource(ingredient):
    resources[ingredient] += 300

def print_report():
    for resource, amount in resources.items():
        if resource == "money":
            print(f"{resource.capitalize()}: ${amount:.2f}")
        else:
            print(f"{resource.capitalize()}: {amount}ml")
    to_add = input("Would you like to add more of an ingredient?: 'yes' or 'no': ")
    if to_add == 'yes':
        resouce_to_add = input("Which ingredient: 'water', 'milk', or 'coffee': ")
        add_resource(resouce_to_add)


def check_resources(drink):
    for ingredient, amount in MENU[drink]['ingredients'].items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def process_coins(drink):
    drink_cost = MENU[drink]["cost"]
    print(f"Your total is: ${drink_cost:.2f}")
    print("Please insert coins.")
    quarter_amt = int(input("How many quarters?: "))
    dime_amt = int(input("How many dimes?: "))
    nickel_amt = int(input("How many nickels?: "))
    penny_amt = int(input("How many pennies?: "))
    total_inserted = (quarter_amt * COINS["QUARTER"] + dime_amt * COINS["DIME"] +
                      nickel_amt * COINS["NICKEL"] + penny_amt * COINS["PENNY"])
    if total_inserted < drink_cost:
        money_needed = drink_cost - total_inserted
        print(f"Sorry, you did not insert enough money. You were ${money_needed:.2f} short. Money refunded.")
    else:
        change_given = total_inserted - drink_cost
        if change_given > 0:
            print(f"Here is your ${change_given:.2f} in change.")
        print(f"Here is your {drink}. Enjoy!")
        process_drink(drink)

def main_screen():
    while True:
        order = input("What would you like? Choose 'espresso', 'latte', or 'cappuccino' (or 'report'/'off'): ")
        if order in MENU:
            if check_resources(order):
                process_coins(order)
        elif order == 'report':
            print_report()
        elif order == 'off':
            break
        else:
            print("Invalid input. Please try again.")

main_screen()