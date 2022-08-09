import random
import math


def is_inside_circle():
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        return True
    else:
        return False

def calculate_pi(iterations, out):
    inside = 0
    for i in range(iterations):
        if is_inside_circle():
            inside += 1
    pi = 4 * inside / iterations
    
    if not out:
        return pi
    else:
        print(f"{iterations} iterations: {pi} ({'{0:+g}'.format(pi - math.pi)})")


for i in range(2, 10):
    calculate_pi(10**i, True)
