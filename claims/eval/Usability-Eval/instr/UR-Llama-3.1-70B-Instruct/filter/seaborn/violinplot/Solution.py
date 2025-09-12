# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Set the style for the plot
sns.set_style("whitegrid")

# Generate a random sample from a normal distribution
np.random.seed(0)
data = np.random.randn(100)

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Draw a KDE plot
sns.kdeplot(data, shade=True, ax=ax)

# Add rug plot for observations
sns.rugplot(data, ax=ax)

# Alternative to add box plot statistics
# sns.boxplot(data, ax=ax)

# Set the title and labels
ax.set_title("KDE with Observations")
ax.set_xlabel("Value")
ax.set_ylabel("Density")

# Show the plot
plt.show()
