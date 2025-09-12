import seaborn as sns
import matplotlib.pyplot as plt

# Load an example dataset
tips = sns.load_dataset('tips')

# Create a simple visualization
sns_plot = sns.scatterplot(data=tips, x='total_bill', y='tip')

# Configure the appearance of tick labels
sns_plot.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:.0f}'))
sns_plot.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0f}% tip'))

plt.show()
