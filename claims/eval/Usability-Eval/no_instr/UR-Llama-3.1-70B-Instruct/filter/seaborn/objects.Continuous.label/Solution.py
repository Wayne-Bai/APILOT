# Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Set the style for the plot
sns.set_style("whitegrid")

# Create a sample figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Create a sample plot
tips = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", data=tips, ax=ax)

# Configure the appearance of tick labels for the scale's axis or legend
ax.tick_params(axis='y', labelsize=8)
ax.set_yticks([2, 4, 6])
ax.set_yticklabels(['$2', '$4', '$6'], fontsize=8)

# Remove the top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Show the plot
plt.show()
