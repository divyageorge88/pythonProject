from Data import Coffee_Menu

def check_resources(choice):
    if choice == "espresso":
        if Coffee_Menu.resources["water"] < Coffee_Menu.MENU["espresso"]["water"] or Coffee_Menu.resources["coffee"] < Coffee_Menu.MENU["espresso"]["coffee"]



users_choice = input("What would you like to have? (espresso/latte/cappuccino):").lower()

if users_choice == "report":
    print(Coffee_Menu.resources)

if users_choice == "off":
    print("Thank you for using Coffee Machine! The machine is turned off.")

if users_choice == "espresso":



