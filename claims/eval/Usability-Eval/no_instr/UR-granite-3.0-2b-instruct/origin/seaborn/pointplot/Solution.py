import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create a dataset
np.random.seed(0)
data = np.random.randn(100, 2)

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot the data with error bars
ax.errorbar(data[:, 0], data[:, 1], yerr=np.abs(data[:, 1]), capsize=3, color='blue', linestyle='--')

# Plot the mean line
ax.plot(data[:, 0], np.mean(data[:, 1]), color='red', linewidth=2)

# Set the plot title and labels
ax.set_title('Point Estimates and Errors')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Show the plot
plt.show()
