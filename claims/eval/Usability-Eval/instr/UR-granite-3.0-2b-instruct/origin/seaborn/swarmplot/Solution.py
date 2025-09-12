import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create a random dataset
np.random.seed(0)
data = np.random.rand(100, 2)
categories = np.random.choice(['A', 'B', 'C'], size=100)

# Create a categorical scatterplot
plt.figure(figsize=(8, 6))
for category, group in zip(categories, data.groupby(categories)):
    plt.scatter(group[:, 0], group[:, 1], label=category, alpha=0.5)

# Adjust points to be non-overlapping
for category in categories:
    category_data = data[categories == category]
    x = category_data[:, 0]
    y = category_data[:, 1]
    plt.scatter(x, y, label=category, alpha=0.5, edgecolor='black')

plt.legend()
plt.show()
