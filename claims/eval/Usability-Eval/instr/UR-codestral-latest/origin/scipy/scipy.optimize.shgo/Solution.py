from scipy.optimize import differential_evolution

def func(x):
    return (x[0] - 1)**2 + (x[1] - 2.5)**2

bounds = [(-5, 5), (-5, 5)]

result = differential_evolution(func, bounds)

print('Global minimum at:', result.x)
print('Function value at the minimum:', result.fun)
