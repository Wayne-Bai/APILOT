# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset
tips = sns.load_dataset("tips")

# Create a figure and axis
fig, ax = plt.subplots()

# Create a barplot with seaborn
sns.barplot(x="sex", y="total_bill", hue="smoker", data=tips, ax=ax)

# Configure the appearance of tick labels for the scale’s axis or legend
plt.xticks(fontsize=10, rotation=45)  # For x-axis
plt.yticks(fontsize=10)  # For y-axis
ax.tick_params(axis='both', labelsize=10)  # For both axes

# Configure the legend
plt.legend(title="Smoker", fontsize=10, title_fontsize=10)

# Show the plot
plt.show()
