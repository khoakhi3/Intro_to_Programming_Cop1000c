kilowattHour = int(input("Enter Kilowatt hours used: "))
if kilowattHour <= 1000:
    owedMoney = (kilowattHour*0.07633)
else:
    owedMoney = ((kilowattHour-1000)*0.09259)+76.33
print("Amount Owed: $", owedMoney)