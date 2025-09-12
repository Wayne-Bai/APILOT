from scipy.optimize import shgo
def objective(x):
 return x[0] ** 2 + x[1] ** 2

bounds = [(0, 10), (0, 10)]
result = shgo(objective, bounds)
print(result)
