import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
tips = sns.load_dataset('tips')

# Draw a categorical scatterplot with non-overlapping points
sns.swarmplot(x='day', y='total_bill', data=tips)

plt.show()
