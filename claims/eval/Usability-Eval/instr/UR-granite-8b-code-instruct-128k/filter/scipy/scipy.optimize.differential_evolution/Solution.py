import scipy.optimize

def objective_function(x):
    # Define your objective function here
    return x[0]**2 + x[1]**2

# Define the initial guess for the optimizer
initial_guess = [0, 0]

# Use the minimize function to find the global minimum
result = scipy.optimize.minimize(objective_function, initial_guess, method='Nelder-Mead')

# Print the result
print(result)
