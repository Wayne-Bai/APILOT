import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
tips = sns.load_dataset('tips')

# Draw the enhanced box plot
ax = sns.boxplot(x='total_bill', y='tip', data=tips, showfliers=False)
sns.swarmplot(x='total_bill', y='tip', data=tips, color='red')
plt.title('Enhanced Box Plot for Tips')
plt.show()
