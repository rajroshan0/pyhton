#from task2 import solve_quad_eq , random_number  #importing previous function from saved python file

import random

def random_number():
    randInt = [random.randint(-100,100) for i in range(3)]
    #(a,b,c) = randInt
   # a= random.randint(-100,100)
   # b= random.randint(-100,100)
   # c= random.randint(-100,100)
    return randInt
a,b,c = random_number()
print(a,b,c)


def solve_quad_eq(a,b,c):
    D = b**2-4*a*c
    if D>0:
        x1 = (-b+(D**1/2))/2*a
        x2 = (-b-(D**1/2))/2*a
        return(x1,x2,D)
    elif D ==0:
        x1=x2=-b/(2*a)
        return (x1,x2,D)
    else:
        return ("noroot")
   

x1, x2, D = solve_quad_eq(a, b, c)
print(solve_quad_eq(a,b,c))
print(x1)
print(x2)
print(D)

print("~"*90)

varF = ("|{0:^31}|".format("Coefficients"))
varS = ("{0:^20}|".format("Discriminant"))
varT = ("{0:^30}|".format("results"))
print(varF,varS,varT)

print("|{0:^9}|".format("a"),"{0:^9}|".format("b"),"{0:^9}|".format("c"),)
print("~"*90)
print("|{0:^9}|".format(a),"{0:^9}|".format(b),"{0:^9}|".format(c),"{0:^19}|".format(D),"{0:^15}|{1:^15}|".format(x1,x2))
print("~"*90)









