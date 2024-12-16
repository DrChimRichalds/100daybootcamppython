

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

"""

"""

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

### Todo- 1 ask user input what they would like
"""Check input to decide what to do next
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.
"""


def menu_options(MENU, coffee_selection):
    if coffee_selection == 'cappuccino':
        print(f" a {coffee_selection} costs {MENU['cappuccino']['cost']}$")
    if coffee_selection == 'espresso':
        print(f" a {coffee_selection} costs {MENU['espresso']['cost']}$")
    if coffee_selection == 'latte':
        print(f" a {coffee_selection} costs {MENU['latte']['cost']}$")
    else:
        print("Not a valid selection")



### Todo-2
"""
Turn off the Coffee Machine by entering “off” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens
"""


### Todo-3
"""
Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
"""
def report(resources, milk_consumed, water_consumed, coffee_consumed):
    resources['water'] -= water_consumed
    resources['milk']  -= milk_consumed
    resources['coffee'] -= coffee_consumed
    print(resources)


### Todo-4
"""
 Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee.
"""
def consume(resources, milk_consumed, water_consumed, coffee_consumed):
    resources['water'] -= water_consumed
    resources['milk']  -= milk_consumed
    resources['coffee'] -= coffee_consumed
    print(resources)

def double_check_resources(resources,coffee_preference):

    temp_milk = resources['milk']
    temp_water = resources['water']
    temp_coffee =resources['coffee']
    temp_milk -= milk_consumed
    if coffee_preference == 'espresso':

    elif coffee_preference == 'latte':

    elif coffee_preference == 'cappuccino':
        return False
    elif temp_water <0:
        return False
    elif temp_coffee < 0:
        return False
    else:
        return True

#double_check_resources(resources, 210, 100, 200 )

###Todo- 5
"""
Process coins.
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
"""
def payment(MENU, coffee_selection):
    print("Payment screen")
    quarters = float(input("How many quarters?"))
    dimes = float(input("How many dimes?"))
    pennies = float(input("How many pennies"))
    total_cash = 0.25*quarters + 0.1*dimes +0.01*pennies
    print(f"Total cash given is {total_cash}")
    latte_price = MENU['latte']['cost']
    espresso_price = MENU['espresso']['cost']
    cappuccino_price = MENU['cappuccino']['cost']
    if coffee_selection == 'espresso' and total_cash>espresso_price:
        return True
    elif coffee_selection == 'cappuccino' and total_cash>cappuccino_price:
        return True
    elif  coffee_selection == 'latte' and total_cash>latte_price:
        return True
    else:
        print("Insufficient funds")
        return False


### Todo-6
"""
 Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “Sorry that's not enough money. Money refunded.”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.
"""

### Todo- 7

"""
Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.
"""

def coffee_machine():
    off= False
    amount_resources = True
    while off == False:
        print("Hello, thank you for building a coffee machine")
        while amount_resources == True:

            coffee_preference = input("What type of coffee would you like? Please type 'Latte', 'espresso', or 'cappuccino' ").lower()
            menu_options(MENU, coffee_preference)
            print("Checking that we have enough resources")
            amount_resources = double_check_resources(resources, coffee_preference )
            check_payment = payment(MENU, coffee_preference)
            while check_payment == False:
                print("Try again, give me more money")
                check_payment = payment(MENU, coffee_preference)
            print("Thank you for your payment")
            make_a_report= input("Would you like a report?").lower()
            if make_a_report == 'yes':
                consume(resources, 10, 10, 10)
            shut_off = input("would you like to turn the machine off? If yes, type 'off'")
            if shut_off == 'off':
                off = True

coffee_machine()
