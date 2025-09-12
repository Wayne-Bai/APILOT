
import matplotlib.pyplot as plt
import seaborn as sns

# Generate some sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
errors = [0.5, 1.0, 1.5, 2.0, 2.5]

# Create a line plot with markers and error bars
sns.lineplot(x=x, y=y, errors=errors, kind='line', marker='o', capsize=5)

# Add labels to the plot
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Point Estimates and Errors')

# Show the plot
plt.show()
