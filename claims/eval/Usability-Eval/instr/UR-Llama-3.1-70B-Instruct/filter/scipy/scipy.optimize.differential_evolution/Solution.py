import scipy.optimize as optimize
import numpy as np

def multivariate_function(x):
    """
    A multivariate function to minimize.
    """
    return x[0]**2 + x[1]**2 + x[2]**2

def main():
    # Initial guess for the minimum
    x0 = np.array([1, 2, 3])

    # Minimize the function using the minimize function from scipy
    result = optimize.minimize(multivariate_function, x0)

    # Print the result
    print("Minimum found at x = ", result.x)
    print("Minimum value: ", result.fun)

if __name__ == "__main__":
    main()
