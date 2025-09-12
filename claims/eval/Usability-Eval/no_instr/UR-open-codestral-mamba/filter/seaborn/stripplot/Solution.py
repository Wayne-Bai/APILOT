import seaborn as sns
import matplotlib.pyplot as plt

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Create a categorical scatterplot with jitter
sns.stripplot(x="total_bill", y="day", data=tips, jitter=True, orient="h")

# Show the plot
plt.show()
