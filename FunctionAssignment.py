#import pi into this doc.
from math import pi
#solve for area of a circle.
def cirArea (r):
    return pi*r**2
#function to calculate total due money.
def totalDue (p, t):
     return p+p*(t/100)
#function to convert F to C.
def FtoC (f):
    return (f-32)*(5/9)
#print out.
radius = float(input("Enter radius: "))
print(round(cirArea(radius), 2))
price = float(input("Enter price: "))
tax = float(input("Enter tax rate: "))
print(round(totalDue(price, tax), 2))
degrees = float(input("Enter degrees: "))
print(round(FtoC(degrees), 2))