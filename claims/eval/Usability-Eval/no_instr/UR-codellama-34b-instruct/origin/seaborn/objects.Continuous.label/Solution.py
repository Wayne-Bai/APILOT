import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = ...

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot data on the axis
sns.heatmap(data, cmap="viridis", ax=ax)

# Configure tick labels for the axis
ax.set_xticklabels(["One", "Two", "Three"])
ax.set_yticklabels(["A", "B", "C"])

# Configure tick labels for the legend
ax.legend(loc="best")
