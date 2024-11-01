import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def euler_method(f, x0, y0, h, num_steps):
    """
    Implements Euler's Method to approximate the solution of a first-order ODE.

    Args:
        f (function): The right-hand side of the differential equation dy/dx = f(x, y).
        x0 (float): The initial value of x.
        y0 (float): The initial value of y.
        h (float): The step size.
        num_steps (int): The number of steps to take.

    Returns:
        list: A list of tuples (x, y) representing the approximated solution.
    """
    x = x0
    y = y0
    solution = [(x0, y0)]

    for _ in range(num_steps):
        y += h * f(x, y)
        x += h
        solution.append((x, y))

    return solution

def parse_ode(ode_string):
    x = sp.Symbol('x')
    y = sp.Function('y')(x)
    ode = sp.Eq(sp.diff(y, x), sp.sympify(ode_string))
    return ode, x, y

def main():
    # Example usage
    def f(x, y):
        return x + y

    x0 = 0
    y0 = 1
    h = 0.1
    num_steps = 10

    solution = euler_method(f, x0, y0, h, num_steps)

    print("Approximated solution:")
    for x, y in solution:
        print(f"x = {x:.1f}, y = {y:.4f}")

if __name__ == "__main__":
    main()