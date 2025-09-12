import scipy.integrate as integrate
import numpy as np

# Define a function to integrate
def func(x):
    return np.sin(x)

# Generate x values
x = np.linspace(0, np.pi, 100)

# Generate y values
y = func(x)

# Define the function with None as x values to assume equal spacing
def func_def_x(x):
    return func(x)

# Integrate using the composite Simpson's rule with x values
result_with_x = integrate.simps(y, x)

# Integrate using the composite Simpson's rule without x values (assuming equal spacing)
result_without_x = integrate.simps(func_def_x(np.linspace(0, np.pi, 100)), dx=(np.pi - 0) / 100)

print(f"Result with x: {result_with_x}")
print(f"Result without x (assuming equal spacing): {result_without_x}")
