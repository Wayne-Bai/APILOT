import seaborn as sns
import matplotlib.pyplot as plt

# Generate some sample data
x = np.random.normal(0, 1, size=50)
y = np.random.normal(0, 1, size=50)

# Create a categorical scatterplot with non-overlapping points
sns.scatterplot(x, y, hue="Category", style="point")

# Adjust the point size and transparency for better visibility
plt.set_size(10)
plt.set_alpha(0.5)

# Show the plot
plt.show()
