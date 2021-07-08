from MENU import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo
from time import sleep

print(logo)
print("WELCOME TO THE COFFEE SHOP")
# Create Objects
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

def making_coffee():
    is_on = True
    while is_on:
        options = menu.get_items()
        choice = input(f"What would you like? {options}: ")
        if choice == "off":
            print("See you next time...")
            is_on = False
        elif choice == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice) # menu_item class
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            else:
                print("Sorry, this machine needs filling...")
                is_on = False


begin = True
while begin:
    print("Refilling...Wait...")
    sleep(2)
    next_customer = input("New customer? 'y' or 'n'")
    if next_customer == 'y':
        making_coffee()
    else:
        break


