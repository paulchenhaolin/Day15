# Solution
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are not enough"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coin():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins")
    total = int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
# Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# need to prompt user everytime they use
# Turn off the Coffee Machine by entering “off” to the prompt


machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            process_coin()

# get three hot flavors 1. espresso (50 ml water, 18g coffee) 2. latte (200 ml water, 24g coffee, 150 ml milk)
# 3. Cappuccino (250 ml water, 24 g coffee, 100 ml milk)
#



#