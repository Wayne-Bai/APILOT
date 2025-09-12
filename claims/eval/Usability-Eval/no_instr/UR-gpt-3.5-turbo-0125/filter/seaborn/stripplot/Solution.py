
import seaborn as sns
import matplotlib.pyplot as plt

# Load a sample dataset for demonstration
tips = sns.load_dataset("tips")

# Draw categorical scatterplot with jitter
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)

# Display the plot
plt.show()
