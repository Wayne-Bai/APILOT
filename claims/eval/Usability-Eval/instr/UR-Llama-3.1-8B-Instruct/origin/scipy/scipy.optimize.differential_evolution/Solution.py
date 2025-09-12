from scipy.optimize import minimize
import numpy as np

# Define the function for which we want to find the global minimum
def func(x):
    # Return the value of the function
    return (x[0] - 1)**2 + (x[1] - 2)**2

# Define the initial guess
x0 = np.array([-3, -3])

# Use the minimize function from scipy to find the global minimum
res = minimize(func, x0)

# Print the result
print('Optimization results:')
print('Number of calls to function: %d' % res.nfev)
print('Total execution time: %.2f seconds' % res.nfev * res.timing.nfun_inv)
print('x: [%f, %f]' % tuple(res.x))
print('f(x): %f' % res.fun)
