import seaborn as sns
import matplotlib.pyplot as plt

# Generate some sample data
x = ['A', 'B', 'C'] * 10
y = [1, 2, 3] * 10 + np.random.randn(30)

# Create a figure and axis object
fig, ax = plt.subplots()

# Draw the scatterplot
sns.stripplot(x=x, y=y, jitter=True, ax=ax)

# Add labels and titles
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Categorical Scatterplot with Jitter')

# Show the plot
plt.show()
