#Simple function which have nothing to call or return except for the print statement.
def printMessage():
    print("i am not returning any values")
 #give the function a parameters or defining the function.
def sum (value1, value2):
    ans = value1 + value2
    return ans
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
#call, run and give function the value to calculate.
finalAnswer = sum(num1, num2) #Assign num1 and num2 for val1 and val2.
print(finalAnswer)

def sequence1 (a):
    ans = (2*a) +3
    return ans
answer = sequence1 (int(input("enter your number: ")))
print("next number in sequence is: ",answer)