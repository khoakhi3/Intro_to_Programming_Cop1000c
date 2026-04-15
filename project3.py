regularSeat = 0
firstClassSeat = 0
emergencySeat = 0
takenSeats = []
def choseSeat ():
    global regularSeat, firstClassSeat, emergencySeat, takenSeats
    while True:
        print("  ******Welcome to United Airline******")
        print("Please review the listing before choosing your seat!")
        print("Seat base price is $500.")
        print("There are 10 rows and total of 20 seats.")
        print("Rows 1-4 are First Class seats and will have additional charge of $200.")
        print("Rows 5-6 are emergency seats with more leg rooms but agreed terms of assisting in case of emergency needed.")
        print("All other rows are Regular Seats and will have no additional charge.")

        try:
            row = int(input("Enter row number (1-10): "))
            seat = int(input("Enter seat number (1 or 2): "))
        except ValueError:
            print("Please enter a number only.")
            continue

        if row < 1 or row > 10 or seat < 1 or seat > 2:
            print("Please choose a valid row and seat.")
            continue

        elif (row, seat) in takenSeats:
            print("The seat you chose is taken, please choose another seat.")
            continue

        elif row >= 1 and row <= 4:
            firstClassSeat +=1
            takenSeats.append((row, seat))
        elif row >= 5 and row <= 6:
            term = input("Do you agree to assist others in case of emergency needed? (y/n): ")
            if term.lower() == "y":
                emergencySeat +=1
                takenSeats.append((row, seat))
            else:
                print("Please choose another seat.")
                continue
        elif row>= 7 and row <= 10:
            regularSeat +=1
            takenSeats.append((row, seat))
        print("Seat booked successfully.")

        again = input("Would you like to buy another seat? (y/n): ").lower()
        if again != "y":
            break

def main():
    choseSeat()
    if firstClassSeat != 0:
        print("First Class seat booked:", firstClassSeat)
    if emergencySeat != 0:
        print("Emergency seat booked:", emergencySeat)
    if regularSeat != 0:
        print("Regular seat booked:", regularSeat)
    if takenSeats != []:
        print("Taken seat booked:")
        for s in takenSeats:
            print("Row:", s[0], "Seat:", s[1])
    total = regularSeat*500 + firstClassSeat*500 + emergencySeat*500 + firstClassSeat*200
    print("Total price booked: $" + str(total))
main()
