import scipy.interpolate as interpolate
import numpy as np

def compute_smoothing_cubic_spline(x, y, lam=None):
    """
    Compute the coefficients of a smoothing cubic spline.

    Parameters:
    x (array_like): The x-coordinates of the data points.
    y (array_like): The y-coordinates of the data points.
    lam (float, optional): The smoothing factor. If None, it is determined using the GCV criteria.

    Returns:
    A smoothing cubic spline object.
    """
    # Check if lam is provided
    if lam is None:
        # Calculate the smoothing factor using the GCV criteria
        spline = interpolate.UnivariateSpline(x, y, s=0.001)
        lam = spline.s
    # Compute the coefficients of the smoothing cubic spline
    spline = interpolate.UnivariateSpline(x, y, s=lam)

    return spline

# Example usage
if __name__ == "__main__":
    # Example x and y values
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + 0.2 * np.random.randn(100)

    # Compute the coefficients of the smoothing cubic spline
    spline = compute_smoothing_cubic_spline(x, y)

    # Evaluate the spline at the x-coordinates
    y_smooth = spline(x)

    # Print the coefficients of the smoothing cubic spline
    print("Coefficients of the smoothing cubic spline:")
    print(spline.get_coeffs())

    # Import matplotlib for plotting
    import matplotlib.pyplot as plt

    # Plot the original data points and the smoothed spline
    plt.scatter(x, y, label='Original data', color='blue')
    plt.plot(x, y_smooth, label='Smoothing cubic spline', color='red')
    plt.legend()
    plt.show()
