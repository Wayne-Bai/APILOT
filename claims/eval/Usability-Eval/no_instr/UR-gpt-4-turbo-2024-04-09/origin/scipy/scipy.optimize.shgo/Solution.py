import scipy.optimize as opt

def objective_function(x):
    return x**2 - 4*x + 4

result = opt.shgo(objective_function, bounds=[(-10, 10)])
print("Global minimum:", result.x)
print("Function value at global minimum:", result.fun)
