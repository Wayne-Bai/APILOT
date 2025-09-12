import scipy.optimize as opt

def my_function(x):
    return x[0]**2 + x[1]**2

result = opt.minimize(my_function, [2, 2])

print("Global minimum:", result.x)
print("Function value at global minimum:", result.fun)
