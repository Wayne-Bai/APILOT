from scipy.interpolate import UnivariateSpline
import numpy as np
from scipy.optimize import curve_fit

# Function to implement the GCV criteria
def gcv(err, m):
    sigma2 = err**2 / ((1 - m/(err.size+m))**2)
    return sigma2

# Sample data
x = np.linspace(0, 10, 20)
y = np.sin(x) + 0.2 * np.random.randn(20)

# Fit the data with the spline interpolate function
lam = None
s = UnivariateSpline(x, y, s=1)
if lam is None:
    # If lam is None, we will use GCV to find it
    sigma2 = gcv(np.abs(s(x) - y), s.get_smooth())
    lam = len(x)*sigma2 / (sigma2+1)
    s = UnivariateSpline(x, y, s=lam)
    
# Display the integral of cos(x) with respect to x
print(s.integral(x.min(), x.max()))

# Plot the data points and the fitted spline
import matplotlib.pyplot as plt
plt.plot(x, s(x), label='Spline')
plt.scatter(x, y, label='Data')
plt.legend()
plt.show()
