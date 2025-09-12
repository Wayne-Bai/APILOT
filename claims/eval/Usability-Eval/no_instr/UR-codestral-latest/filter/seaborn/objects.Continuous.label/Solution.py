import seaborn as sns
import matplotlib.pyplot as plt

# Load a dataset (for example, tips dataset from seaborn)
tips = sns.load_dataset("tips")

# Create a line plot
sns.lineplot(x="total_bill", y="tip", data=tips)

# Configure the appearance of tick labels
plt.xticks(fontsize=12) # change the fontsize of x-axis tick labels
plt.yticks(fontsize=12) # change the fontsize of y-axis tick labels

# Show the plot
plt.show()
