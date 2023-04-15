import random

def random_number():
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    c = random.randint(-100, 100)
    return a, b, c

print(random_number())

def solve_quad_eq(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + (D ** 0.5)) / (2 * a)
        x2 = (-b - (D ** 0.5)) / (2 * a)
        return x1, x2
    elif D == 0:
        x1 = x2 = -b / (2 * a)
        return x1, x2
    elif D < 0:
        return "absence of real roots in the equation"
    else:
        return "no roots"

print(solve_quad_eq(*random_number()))
