import random
import math


def is_inside_circle():
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        return True
    else:
        return False

def calculate_pi(iterations):
    inside = 0
    for i in range(iterations):
        if is_inside_circle():
            inside += 1
    pi = 4 * inside / iterations
    print(f"{iterations} iterations: {pi} ({pi - math.pi})")


for i in range(2, 9):
    calculate_pi(10**i)
