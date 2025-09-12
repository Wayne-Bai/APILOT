from scipy.optimize import minimize

# Define the multivariate function
def fun(x):
    return (x[0]-1)**2 + (x[1]-2.5)**2

# Define the initial guess
x0 = [0, 0]

# Use the minimize function to find the minimum
res = minimize(fun, x0)

print("The global minimum occurs at:", res.x)
