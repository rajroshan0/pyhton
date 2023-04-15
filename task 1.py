import random

def generate_random_integers():
    # Generate three random integers in the range of -100 to 100
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    c = random.randint(-100, 100)
    
    # Return the generated integers as a tuple
    return a, b, c
print(generate_random_integers())

def solve_quadratic_equation(a, b, c):
    # Calculate the discriminant
    D = b**2 - 4*a*c
    
    # Check if the discriminant is positive, negative, or zero
    if D > 0:
        # Two roots
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        return x1, x2
    elif D == 0:
        # Two identical roots
        x1 = x2 = -b / (2*a)
        return x1, x2
    else:
        # No roots
        return "No roots"

