import scipy.optimize

# Define the function to be fitted
def f(x, a, b):
    return a * x + b

# Generate some data to fit
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 6, 8, 10]

# Define the initial guess for the parameters
initial_guess = [1, 1]

# Perform the non-linear least squares fit
result = scipy.optimize.curve_fit(f, x_data, y_data, initial_guess)

# Print the result
print("Optimal parameters: a = {}, b = {}".format(result[0][0], result[0][1]))
