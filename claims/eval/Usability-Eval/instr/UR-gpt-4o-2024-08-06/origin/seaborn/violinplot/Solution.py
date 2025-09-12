import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create sample data
np.random.seed(10)
data = np.random.normal(size=100)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot a KDE with seaborn
sns.kdeplot(data, fill=True, ax=ax, color="skyblue", alpha=0.5)

# Overlay a strip plot for individual observations
sns.stripplot(data, color='red', jitter=True, size=4, alpha=0.7, ax=ax)

# Overlay a box plot to show summary statistics
sns.boxplot(data, color='lightgreen', width=0.1, fliersize=0, ax=ax)

# Display the plot
plt.show()
