import scipy.optimize as opt

def objective_function(x):
    return x**2 + 10 * np.sin(x)

result = opt.shgo(objective_function, bounds=[(-10, 10)])
print("Global minimum:", result.x, "Value:", result.fun)
