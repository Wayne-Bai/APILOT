import seaborn as sns
import matplotlib.pyplot as plt

# Load a dataset
tips = sns.load_dataset("tips")

# Create a barplot
ax = sns.barplot(x="day", y="total_bill", data=tips)

# Configure the appearance of tick labels for the scale's axis
ax.set_xlabel("Day of the Week", fontsize=14)
ax.set_ylabel("Total Bill ($)", fontsize=14)

# Configure the appearance of tick labels for the legend
ax.legend(title="Day of the Week", prop={'size': 12})

# Display the plot
plt.show()
