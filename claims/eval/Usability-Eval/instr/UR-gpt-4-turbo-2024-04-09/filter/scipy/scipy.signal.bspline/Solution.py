import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

def plot_b_spline_basis(knots, degree):
    # Create a range of x values for plotting the B-spline
    x = np.linspace(knots[0], knots[-1], num=400)
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Calculate and plot the B-spline basis functions for each knot interval
    for i in range(len(knots) - degree - 1):
        t = knots[i:i + degree + 2]  # Local knot vector
        spl = BSpline.basis_element(t, extrapolate=False)
        y = spl(x)
        ax.plot(x, y, label=f'B-spline basis {i + 1}')
    
    # Setting the plot title and labels
    ax.set_title(f'B-spline Basis Functions of Degree {degree}')
    ax.set_xlabel('x')
    ax.set_ylabel('B-spline value')
    ax.legend()
    
    # Show the plot
    plt.show()

# Example usage
knots = np.array([0, 1, 2, 3, 4, 5, 6])
degree = 2  # Quadratic B-splines
plot_b_spline_basis(knots, degree)
