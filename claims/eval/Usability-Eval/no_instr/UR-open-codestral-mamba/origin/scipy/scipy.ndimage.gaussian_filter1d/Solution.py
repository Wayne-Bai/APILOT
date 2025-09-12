import scipy.ndimage as ndi
import numpy as np

# create a 1-dimensional signal
N = 100
x = np.linspace(0, 10, N)
y = np.sin(x) + np.random.randn(N)

# apply 1-D Gaussian filter
sigma = 1.0
y_filt = ndi.gaussian_filter1d(y, sigma)

# plot original and filtered signals
import matplotlib.pyplot as plt

plt.plot(x, y, label='Original Signal')
plt.plot(x, y_filt, label='Filtered Signal')
plt.legend(loc='best')
plt.title('1-D Gaussian Filter (SciPy)')
plt.show()
