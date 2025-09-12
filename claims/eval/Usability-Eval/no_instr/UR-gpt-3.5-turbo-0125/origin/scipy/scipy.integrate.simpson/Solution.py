
import numpy as np

def simpson_integral(y, x=None, dx=None):
    if x is None:
        if dx is None:
            raise ValueError("If x is None, dx cannot be None")

        x = np.arange(len(y)) * dx

    if len(y) < 3:
        raise ValueError("At least 3 samples are needed for Simpson's rule")

    integral = 0
    for i in range(0, len(y) - 2, 2):
        h = x[i+2] - x[i]
        integral += (h/3) * (y[i] + 4*y[i+1] + y[i+2])

    if len(y) % 2 == 0:  # Handling the case when number of samples is even
        integral += (h/3) * (y[-2] + y[-1])

    return integral

# Example usage
y_values = [1, 2, 3, 4, 5]
integral_result = simpson_integral(y_values, dx=1)
print("Integral using Simpson's rule:", integral_result)
