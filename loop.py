heartWants = int(input("How many times do you love me?"))
runThisLoop = 0

while (runThisLoop < heartWants):
    print("I love you this many times") #Will run forever if never break.
    runThisLoop = runThisLoop + 1 #Add value to variable until it break the loop.

groceryList = ["apple", "banana", "cherry", "eggs", "bread"]
for item in groceryList:
    print(item)