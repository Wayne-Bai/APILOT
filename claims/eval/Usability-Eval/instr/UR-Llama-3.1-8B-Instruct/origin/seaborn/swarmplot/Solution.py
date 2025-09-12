# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set a seed for reproducibility
np.random.seed(0)

# Generate some sample data
x = np.random.choice(['A', 'B', 'C'], 50)
y = np.random.uniform(0, 10, 50)
_Category = np.random.choice(['Category 1', 'Category 2', 'Category 3'], 50)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a categorical scatterplot with points adjusted to be non-overlapping
sns.scatterplot(x=_Category, y=y, ax=ax, hue=_Category, palette="Set2", legend=False)

# Customize the plot
ax.set_xlabel('')
ax.set_ylabel('Value')
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot
plt.show()
