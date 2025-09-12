import seaborn as sns
import matplotlib.pyplot as plt

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a figure with two subplots
fig, ax = plt.subplots(2, 1, figsize=(8, 10))

# Plot the KDE on the first subplot
sns.kdeplot(data=tips, x="total_bill", ax=ax[0], fill=True)
ax[0].set_title("KDE Plot of Total Bill")

# Plot the boxplot on the second subplot
sns.boxplot(data=tips, x="total_bill", ax=ax[1])
ax[1].set_title("Box Plot of Total Bill")

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
