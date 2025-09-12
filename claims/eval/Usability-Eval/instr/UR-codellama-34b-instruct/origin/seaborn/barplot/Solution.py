
import seaborn as sns
import matplotlib.pyplot as plt

# Data for the plot
x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]
error = [1, 2, 3, 4, 5]

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the data as points with error bars
ax.scatter(x, y, color='red')
ax.errorbar(x, y, yerr=error, fmt='o', ecolor='gray')

# Set the axis labels and title
ax.set_xlabel('X-axis label')
ax.set_ylabel('Y-axis label')
ax.set_title('Point estimates with error bars')

# Show the plot
plt.show()
