import seaborn as sns
import matplotlib.pyplot as plt

# Example data
data = sns.load_dataset("tips")

# Create a plot
sns.scatterplot(x="total_bill", y="tip", data=data)

# Configure the appearance of tick labels for the x-axis
plt.xticks(fontsize=10, rotation=45)

# Configure the appearance of tick labels for the y-axis
plt.yticks(fontsize=10)

# Show the plot
plt.show()
