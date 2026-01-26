print("Khoa Duong")

name = "Scooby" #Variables unlike other languages dont have a type.
#int (Whole number), double (Double the float), float (Decimal number beyond 7 digits), char (1 single letter or character), string (group of letters, words), boolean (true or false)
age = 21
temperature = 60
#Types of printing
print("I am {} years old, and the temperature is {} degrees".format(age, temperature))#Tell python the format we wanted it in.

#input
friendName = input("What is your name?\n ") #\ is escape character, n meant new line.
print("The new friend name is", friendName)

friendAge = int(input("What is your age?\n ")) #int to tell python that you wanted a whole number, not string.
print("He is {} years old".format(friendAge))

#input
total = 52 +78
print(total)
agesTotal = friendAge + total
print(agesTotal)

