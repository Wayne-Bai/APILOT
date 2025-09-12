from scipy.optimize import shgo

def func(x):
    return (x[0] - 1)**2 + (x[1] - 2.5)**2

bounds = [(0, 5), (0, 5)]
result = shgo(func, bounds)
print(result.x, result.fun)
