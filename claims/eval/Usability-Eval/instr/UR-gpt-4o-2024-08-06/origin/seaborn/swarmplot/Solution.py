import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset('tips')

# Create the categorical scatterplot with jittering for non-overlapping points
sns.catplot(x='day', y='total_bill', data=data, kind='strip', jitter=True, height=6, aspect=1)

# Show plot
plt.show()
