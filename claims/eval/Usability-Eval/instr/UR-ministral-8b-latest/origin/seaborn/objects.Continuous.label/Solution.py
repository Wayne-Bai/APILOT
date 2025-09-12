import seaborn as sns
import matplotlib.pyplot as plt

# Load a sample dataset
tips = sns.load_dataset("tips")

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot a bar plot
sns.barplot(ax=ax, data=tips, x="day", y="total_bill")

# Step 1: Configure tick labels for the x-axis
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

# Step 2: Configure tick labels for the y-axis (optional)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, horizontalalignment='right')

# Step 3: Configure the appearance of the legend labels (optional)
for handle, image in zip(ax.get_legend_handles_labels()[0], ax.get_legend_handles_labels()[1]):
    ax.annotate(image, xy=handle.get_position(), textcoords='offset points', xytext=(10,0), ha='left', fontsize=12)

# Display the plot
plt.show()
