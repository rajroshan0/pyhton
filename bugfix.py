import random
import random

def random_number():
    randInt = [random.randint(-100,100) for i in range(3)]
    return randInt

a, b, c = random_number()
print("a =", a)
print("b =", b)
print("c =", c)


a,b,c = [3,53,5]
print(a,b,c)
