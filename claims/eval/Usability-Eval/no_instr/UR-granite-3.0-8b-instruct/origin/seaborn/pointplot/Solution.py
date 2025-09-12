import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a DataFrame `df` with columns 'x', 'y', 'lower', and 'upper'
# 'x' and 'y' are the point estimates, and 'lower' and 'upper' are the error bounds

# Create a scatter plot with markers
plt.scatter(df['x'], df['y'], marker='o', label='Point Estimates')

# Create a line plot with markers for the error bounds
plt.plot(df['x'], df['lower'], marker='o', linestyle='--', label='Lower Bound')
plt.plot(df['x'], df['upper'], marker='o', linestyle='--', label='Upper Bound')

# Add a legend
plt.legend()

# Show the plot
plt.show()
