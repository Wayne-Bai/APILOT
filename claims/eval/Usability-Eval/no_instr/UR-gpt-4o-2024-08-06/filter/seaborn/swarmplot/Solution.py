import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset('tips')

# Draw a categorical scatterplot using seaborn's 'stripplot'
# with 'jitter' parameter to adjust points to be non-overlapping
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)

# Display the plot
plt.show()
