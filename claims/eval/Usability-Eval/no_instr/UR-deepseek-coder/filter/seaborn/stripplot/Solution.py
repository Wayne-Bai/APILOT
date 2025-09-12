import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Draw a strip plot with jitter
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)

# Show the plot
plt.show()
