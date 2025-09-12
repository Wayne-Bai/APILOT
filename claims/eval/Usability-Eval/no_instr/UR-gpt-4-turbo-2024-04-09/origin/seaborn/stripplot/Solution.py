import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Create a strip plot with jitter
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)

# Display the plot
plt.show()
