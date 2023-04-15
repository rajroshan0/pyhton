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
    elif D< 0:
        return ("absence of real Root in the equation",D)
    else:
        return "noroots",D

x1, x2, D = solve_quad_eq(a, b, c)
print(solve_quad_eq(a,b,c))
print(x1)
print(x2)
print(D)





