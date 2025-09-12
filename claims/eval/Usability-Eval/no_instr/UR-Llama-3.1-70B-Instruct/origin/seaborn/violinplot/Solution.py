# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create a sample dataset
np.random.seed(0)
data = np.random.randn(100)

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a KDE plot with observations
sns.kdeplot(data, ax=ax, fill=True)

# Add observations as rug plot
sns.rugplot(data, ax=ax)

# Alternatively, you can add box plot statistics
# sns.boxplot(data, ax=ax)

# Set title and labels
ax.set_title('KDE Plot with Observations')
ax.set_xlabel('Value')
ax.set_ylabel('Density')

# Show the plot
plt.show()
