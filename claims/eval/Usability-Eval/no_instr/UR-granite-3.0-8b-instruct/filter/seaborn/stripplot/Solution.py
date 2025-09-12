import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Create a strip plot with jitter
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True, size=4)

# Add a box plot on top of the strip plot
sns.boxplot(x="day", y="total_bill", data=tips, color="white")

plt.show()
