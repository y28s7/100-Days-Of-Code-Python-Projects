# Imports:
from data import MENU, profit, resources

# Variables:
turn_off = False
can_buy = False


# Other Functions:

def process_coins():
    # TODO 5: Ask user for coins and process them
    print("Please insert your coins below: ")
    quarters = int(input("  Quarters: "))
    dimes = int(input("  Dimes: "))
    nickels = int(input("  Nickels: "))
    pennies = int(input("  Pennies: "))
    return round(((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)), 2)


def check_resources(ingredients, current_resources):
    # TODO 4: Check if there are enough resources to make the coffee, and if there isn't, give feedback to the user
    for item in ingredients:
        if ingredients[item] > current_resources[item]:
            print(f"Sorry, there's not enough {item}")
            return False
    return True


def add_profit(total, drink_cost):
    # TODO 6: Check if the transaction is successful:
    #   TODO 6A: If there are too little coins, refund and tell user
    if total < drink_cost:
        print("Not enough money. Coins have been refunded.")
        return
    elif total >= drink_cost:
        global profit
        profit += drink_cost
        #   TODO 6B: If there are too many coins, give change
        change = round(total - drink_cost, 2)
        print(f"Here is your change of ${change}.")


def report_resources(current_resources, money):
    print(f"Water: {current_resources['water']}ml")
    print(f"Milk: {current_resources['milk']}ml")
    print(f"Coffee: {current_resources['coffee']}g")
    print(f"Money: ${money}")
    return


def make_coffee(needed_resources, choice):
    # TODO 7: Make the coffee and deduct resources. Then give feedback such as "Here's your coffee!"
    global resources
    resources["water"] = resources["water"] - needed_resources["water"]
    resources["milk"] = resources["milk"] - needed_resources["milk"]
    resources["coffee"] = resources["coffee"] - needed_resources["coffee"]
    print(f"Here's your {choice}! ☕")


def game():
    global profit
    global turn_off
    # TODO 1: prompt the user to insert what type of drink, espresso, latte, or cappuccino
    choice = input("What drink do you want to order? Espresso/Latte/Cappuccino: ").lower()

    # TODO 2: Turn off coffee machine with keyword "off"
    if choice == "off":
        turn_off = True
        return
    # TODO 3: Print report of resources and money in coffee machine with keyword "report"
    elif choice == "report":
        report_resources(resources, profit)
        return
    else:
        drink_ingredients = MENU[choice]["ingredients"]
        drink_cost = MENU[choice]["cost"]

    if not check_resources(drink_ingredients, resources):
        return

    total = process_coins()

    add_profit(total, drink_cost)

    make_coffee(drink_ingredients, choice)


# TODO 8: Make the machine run in a loop and so that it only turns off when you type "off"
while not turn_off:
    game()
