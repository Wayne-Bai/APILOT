import numpy as np
import scipy.integrate
import scipy.interpolate

def composite_simpson_N(y, interval, n):
    # Ensure the integrand y is interpolated
    x = np.linspace(interval[0], interval[1], n+1)
    y_vals = y(x)
    interpolating_function = scipy.interpolate.interp1d(x, y_vals, kind='linear')

    # Simpson's rule with composite trapezoidal
    def integrand(i):
        return interpolating_function(interval[0] + (i-1) * ((interval[1] - interval[0]) / n))

    return scipy.integrate.simps([integrand(i) for i in range(1, n)], dx=(interval[1] - interval[0]) / n)

def integrand(y, interval):
    return y(interval[0] + (interval[1] - interval[0]) / 2)

def integrate_y(y, interval=None, n=3):
    if interval is None:
        spacing = 1  # assumed spacing
        interval = (-spacing, spacing)
    return scipy.integrate.simps(composite_simpson_N(y, interval, n), dx=(interval[1] - interval[0]) / n)

# Example usage:
if __name__ == "__main__":
    def f(x):
        return np.cos(x)

    f_value = integrate_y(f, interval=(-np.pi, np.pi), n=10)
    print(f"Integral value: {f_value}")
