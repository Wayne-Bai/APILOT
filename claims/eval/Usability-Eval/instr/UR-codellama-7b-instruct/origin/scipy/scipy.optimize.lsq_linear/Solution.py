
import numpy as np
from scipy.optimize import minimize

def least_squares(x, y):
    return (x - np.mean(x)) * (y - np.mean(y))

def bounds(a, b, c):
    return [a - c, b + c]

def solve_least_squares_problem(x, y, a, b, c):
    res = minimize(least_squares, x, args=(y,), method="SLSQP", bounds=bounds(a, b, c))
    return res.x
