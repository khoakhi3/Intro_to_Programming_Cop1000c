#Create an object for beverages and their prices.
#Create an object for vending machine including adding beverages and their prices.
#Create a Menu showing beverages and prices.
#Create a main function to get user's input and calculates prices.
#Have to make sure menu is looping and user can insert more money if needed.
class Beverages:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class VendingMachine:
    def __init__(self):
        self.Beverages = []
        self.Beverages.append(Beverages("Coke", 2.00))
        self.Beverages.append(Beverages("Root Beer", 2.50))
        self.Beverages.append(Beverages("Water Bottle", 1.50))
        self.Beverages.append(Beverages("Coffee", 2.50))
        self.Beverages.append(Beverages("Green Tea", 3.00))
        self.Beverages.append(Beverages("Fresh Juice", 4.00))
def menu():
    print("   --WELCOME--")
    print("Menu:")
    print("1. Coke - $2.00")
    print("2. Root Beer - $2.50")
    print("3. Water Bottle - $1.50")
    print("4. Coffee - $2.50")
    print("5. Green Tea - $3.00")
    print("6. Fresh Juice - $4.00")
    print()
def main():
    machine = VendingMachine()
    while True:
        menu()
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            drink = machine.Beverages[0]
        elif choice == "2":
            drink = machine.Beverages[1]
        elif choice == "3":
            drink = machine.Beverages[2]
        elif choice == "4":
            drink = machine.Beverages[3]
        elif choice == "5":
            drink = machine.Beverages[4]
        elif choice == "6":
            drink = machine.Beverages[5]
        else:
            print("Please enter a valid option")
            continue
        print ("Price is: $", drink.price)
        money = float(input("Enter the amount of money: "))

        if money == drink.price:
            print("Here is your", drink.name)
            print("Your change is: $", format(money - drink.price, ".2f"))
        elif money < drink.price:
            while money < drink.price:
                print("Not enough money!! Please insert more money.")
                additionMoney = float(input("Enter the amount of money: "))
                money += additionMoney
            print("Here is your", drink.name)
            print("Your change is: $", format(money - drink.price, ".2f"))
        else:
            print("Here is your", drink.name)
            print("Here is your change: $", format(money - drink.price, ".2f"))
        print("--Thank you for coming--")
        print()
main()