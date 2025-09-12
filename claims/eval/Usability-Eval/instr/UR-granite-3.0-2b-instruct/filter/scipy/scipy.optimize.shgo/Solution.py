from scipy import optimize

# Define the function for which you want to find the global minimum
def function_to_minimize(x):
    # Replace this with your actual function
    return (x**2 - 3*x + 2) ** 2

# Use the SHG (Simulated Hydrogen Gas) optimization algorithm to find the global minimum
result = optimize.minimize(function_to_minimize, 0, method='SHG')

# Print the result
print("The global minimum is at x =", result.x)
print("The minimum value is:", result.fun)
