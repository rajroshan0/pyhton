from random import randint
import statistics as st
import numpy as np


def addition_fun(x,y):#function for addition operation
    z=(x+y)**2
    print(z)
addition_fun(7363,254374)

def paswanFunc(*rajArg):
    result = rajArg *3
    return(result)
print (paswanFunc(1,2))
print (paswanFunc(2,3,5,2,5,3))
print(paswanFunc("raj","roshan","paswan","kumar"))


myVar = 0
if myVar > 0:
    print("myVar is greater than 0") #if true print the string inside the bracket
print("it's less then 0") #instead of else we can direclty use  print for other instances




raj=0
if raj>0:
    print("raj is more than 0")
else:
    print("raj is less than 0")


roshan=0
if roshan > 0:
    print("roshan is greater than 0")
elif roshan == 10:
    print("roshan is equal to 10")
elif roshan == 0 :
    print("roshan is exactly equal to 0")
else:
    print("roshan is less than 0")


raj = 23
if raj>0:
    if raj>20:
        print("raj is greater than 20(0-20_)")
    elif raj <100:
        print("raj is less than 100  ")
elif raj> 50:
    if raj<70:
        print("raj is greater than 70 too")
    else:
        print("number is over 50 and ")
else:
    print("number is less than or ewual to zero")

myVar = 0

if myVar > -2 or myVar <2:
    print("myVar is in (-2,2) interval ")



def threeRandInt():
    sample = [randint(-100,100) for i in range(3)]
    return(sample)
print(threeRandInt()) # generated three random int









