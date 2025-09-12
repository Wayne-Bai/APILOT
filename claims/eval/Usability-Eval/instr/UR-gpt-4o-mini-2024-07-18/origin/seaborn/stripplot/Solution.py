import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset('tips')

# Draw a categorical scatterplot using jitter
sns.catplot(x='day', y='total_bill', data=data, jitter=True, kind='strip')

plt.show()
