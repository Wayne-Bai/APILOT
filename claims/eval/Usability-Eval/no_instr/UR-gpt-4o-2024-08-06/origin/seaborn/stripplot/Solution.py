import seaborn as sns
import matplotlib.pyplot as plt

# Example dataset
tips = sns.load_dataset('tips')

# Create a categorical scatter plot (strip plot) with jitter to reduce overplotting
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)

# Show plot
plt.show()
