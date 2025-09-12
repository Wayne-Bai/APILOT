import scipy.optimize

def my_function(x):
    # replace with your function
    return x[0]**2 + x[1]**2

# Initial guess for the solution
x0 = [1, 1]

# Minimizing using the L-BFGS-B algorithm
res = scipy.optimize.minimize(my_function, x0, method='L-BFGS-B')

print(res.x)  # This will print the optimal solution found
