import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
np.random.seed(0)
data = np.random.randn(100)

# Create a scatter plot with Seaborn
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# Plot the data points with error bars using points and markers
sns.scatterplot(x=np.arange(len(data)), y=data, ax=plt.gca())

# Show the estimated mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data)

# Calculate point estimates and errors
x_estimates = np.arange(-10, 15)
y_estimates = mean + x_estimates * (std_dev / np.sqrt(100 / 2))

# Add error bars using plt.errorbar
plt.errorbar(x=np.arange(len(data)), y=data, xerr=np.sqrt(np.var(data)/len(data)), fmt='o', color='red', capsize=5)

# Add a line for the estimated mean
plt.plot(x_estimates, y_estimates, linestyle='-', color='blue', label=f'Mean ± 1 SE: {mean:.2f} ± {std_dev / np.sqrt(len(data)):.2f}')

# Show the plot with appropriate labels and title
plt.xlabel('Data Points')
plt.ylabel('Values')
plt.title('Scatter Plot with Point Estimates and Errors')
plt.legend()
plt.show()
