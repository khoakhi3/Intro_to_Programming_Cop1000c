
def main():
    print("Welcome to Taco Palace! ")
    print("Please view the menu below")
    print("and make a selection.")
    getOrder()
def getOrder ():
    total = 0
    ordered = []
    taco = 5.00
    burrito = 7.50
    nachos = 2.50
    softDrink = 1.50

    while True:
        menuOptions()
        a = int(input("Enter your selection: "))
        if a == 1:
            print("You have selected Taco")
            total += taco
            print("Your current balance is $", total)
            ordered.append("Taco")
        elif a == 2:
            print("You have selected Burrito")
            total += burrito
            print("Your current balance is $", total)
            ordered.append("Burrito")
        elif a == 3:
            print("You have selected Nachos")
            total += nachos
            print("Your current balance is $", total)
            ordered.append("Nachos")
        elif a == 4:
            print("You have selected Soft Drink")
            total += softDrink
            print("Your current balance is $", total)
            ordered.append("Soft Drink")
        elif a == 5:
            break
        else:
            print("Please enter valid input")
    if len(ordered) == 0:
        print("Sorry, you have not ordered.")
    elif len(ordered) == 1:
        print("You have ordered", ordered[0])
    else:
        print("You have ordered", ",".join(ordered[:-1]), "and", ordered[-1])
    print ("Your total balance is $", total)

def menuOptions ():

    print("Taco Palace Menu:")
    print("1. Taco... 5.00")
    print("2. Burrito... 7.50")
    print("3. Nachos... 2.50")
    print("4. Soft Drink... 1.50")
    print("5. Exit")

main()