import seaborn as sns
import matplotlib.pyplot as plt

# Example data
tips = sns.load_dataset("tips")

# Creating a categorical scatterplot with adjusted points
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)

# Show the plot
plt.show()
