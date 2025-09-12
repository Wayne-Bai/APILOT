from scipy.integrate import simps
from numpy import linspace

def integrate_y(x, y, dx=1.0):
    if x is None:
        x = linspace(0, (len(y)-1)*dx, len(y))
    return simps(y, x)

# Test the function
x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 1, 4, 2]

integral = integrate_y(x_values, y_values)
print("The integral of y(x) using Simpson's rule is: ", integral)
