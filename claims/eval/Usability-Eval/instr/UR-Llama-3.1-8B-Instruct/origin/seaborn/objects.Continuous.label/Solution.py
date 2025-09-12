# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset('tips')

# Create a scatter plot
plt.figure(figsize=(10,6))
sns.scatterplot(x="total_bill", y="tip", data=tips)

# Configure the appearance of tick labels
plt.xticks(fontsize=12, rotation=45)  # rotate and increase font size of xtick labels
plt.yticks(fontsize=12)  # increase font size of ytick labels

# Customizing font style and color of tick labels
plt.xlabel("Total Bill", fontsize=14, fontweight='bold')  # Customizing x-axis label
plt.ylabel("Tip", fontsize=14, fontweight='bold')  # Customizing y-axis label

# Show the legend only for scatterplot
sns.scatterplot(x="total_bill", y="tip", data=tips, label="Scatter plot")  # Assigning a label to the scatterplot
plt.legend(title="Legend", loc='upper right', bbox_to_anchor=(1.2, 1.0), fontsize=12, fancybox=True)  # Adding custom legend

# Show the plot
plt.tight_layout()
plt.show()
