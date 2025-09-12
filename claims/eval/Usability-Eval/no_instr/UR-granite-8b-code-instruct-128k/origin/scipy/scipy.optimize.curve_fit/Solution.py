import scipy.optimize as opt

# Define the function to fit
def f(x, a, b, c):
    return a * x ** 2 + b * x + c

# Generate some sample data
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# Use non-linear least squares to fit the function to the data
popt, pcov = opt.curve_fit(f, x, y)

# Print the fitted parameters
print('a =', popt[0])
print('b =', popt[1])
print('c =', popt[2])
