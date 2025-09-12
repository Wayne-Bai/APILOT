import scipy.optimize as optimize
import numpy as np

# Define the objective function to minimize
def objective_function(x):
    # For example, we want to minimize the function f(x, y) = x^2 + y^2
    return x[0]**2 + x[1]**2

# Define the bounds for the variables
bounds = [(-10, 10), (-10, 10)]

# Initialize the initial guess
initial_guess = [1, 1]

# Define the differential evolution parameters
diff_evolution_params = {
    '(strategy)': 'best1bin',
   'maxiter': 1000,
    'popsize': 50,
    'tol': 1e-5,
   'mutation': (0.5, 1),
   'recombination': 0.7,
   'seed': 0
}

# Use differential evolution to find the global minimum
res = optimize.differential_evolution(
    objective_function, 
    bounds, 
    x0=initial_guess,
    **diff_evolution_params)

print("Global minimum at:", res.x)
print("Global minimum function value:", res.fun)
