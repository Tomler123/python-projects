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

question = "What would you like? (espresso/latte/cappuccino): "
total = 0
report = """Water: %s\nMilk: %s\nCoffee: %s\nMoney: $%s""" % (resources.get("water"), resources.get("milk"), resources.get("coffee"), "{:.2f}".format(total))

print(report)

def checker(coffee):
    if(coffee == "espresso"):
        return resources.get("water") >= MENU.get(coffee).get("ingredients").get("water")  and resources.get("coffee") >= MENU.get(
            coffee).get("ingredients").get("coffee")
    else:
        return resources.get("water") >= MENU.get(coffee).get("ingredients").get("water") and resources.get("milk") >= MENU.get(coffee).get("ingredients").get("milk") and resources.get("coffee") >= MENU.get(coffee).get("ingredients").get("coffee")

insert = "Please insert coins."

while(True):
    choice = input(question)


    if(choice == "latte" or choice == "cappuccino" or choice == "espresso"):
        if(checker(choice)):
            quarters = float(input("How many quarters? "))*0.25
            dimes = float(input("How many dimes? "))*0.1
            nickles = float(input("How many nickles? "))*0.05
            pennies = float(input("How many pennies? "))*0.01

            inserted = quarters + dimes + nickles + pennies
            if(MENU.get(choice).get("cost") <= inserted):
                print("Here is your change " + str("{:.2f}".format(float(inserted) - (float(MENU.get(choice).get('cost'))))))
                print("Here is your " + choice + " Enjoy!")
                total = total + float(inserted) - (float(MENU.get(choice).get('cost')))
                if(choice != "espresso"):
                    resources.update({"milk" : resources.get("milk") - MENU.get(choice).get("ingredients").get("milk")})
                resources.update({"water" : resources.get("water") - MENU.get(choice).get("ingredients").get("water")})
                resources.update({"coffee" : resources.get("coffee") - MENU.get(choice).get("ingredients").get("coffee")})

            else:
                print("Insufficient money. Cost: " + str(MENU.get(choice).get("cost")) + " Inserted: " + str(inserted))
        else:
            print("Insufficient resources")
    elif(choice == "report"):
        print("""Water: %s\nMilk: %s\nCoffee: %s\nMoney: $%s""" % (resources.get("water"), resources.get("milk"), resources.get("coffee"), "{:.2f}".format(total)))
    elif(choice == "break"):
        break
    else:
        print("Name not found")