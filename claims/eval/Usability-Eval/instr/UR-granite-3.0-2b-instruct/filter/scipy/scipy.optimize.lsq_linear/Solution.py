from scipy.optimize import least_squares

# Define the function to be minimized
def residuals(x, A, b):
    return A.dot(x) - b

# Define the bounds for the variables
bounds = [(0, None), (0, None)]

# Define the data
A = [[3, 2], [2, 3]]
b = [6, 8]

# Solve the linear least-squares problem
x0 = least_squares(residuals, [0, 0], args=(A, b), bounds=bounds)

# Print the solution
print("The solution is:", x0.x)
