#Day-15-CoffeeMachine

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(need_input):
    for i in MENU[need_input]['ingredients']:
        if MENU[need_input]['ingredients'][i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


def check_money(need_input, total):
    if total < MENU[need_input]['cost']:
        print("“Sorry that's not enough money. Money refunded.")
        return False
    else:
        return True


def consume_resources(need_input):
    for i in MENU[need_input]['ingredients']:
        resources[i] -= MENU[need_input]['ingredients'][i]


machine_on = True
money = 0
while machine_on:
    need = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if need == "off":
        machine_on = False
    elif need == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        if check_resources(need):
            print("Please insert coins.")
            quarter_cnt = int(input("how many quarters?: "))
            dime_cnt = int(input("how many dimes?: "))
            nickle_cnt = int(input("how many nickles?: "))
            penny_cnt = int(input("how many pennies?: "))
            ttl = quarter_cnt * 0.25 + dime_cnt * 0.1 + nickle_cnt * 0.05 + penny_cnt * 0.01
            if check_money(need, ttl):
                change = round(ttl - MENU[need]['cost'], 2)
                money += MENU[need]['cost']
                print(f"Here is ${change} dollars in change.")
                consume_resources(need)
                print(f"Here is your {need}. Enjoy!☕")
