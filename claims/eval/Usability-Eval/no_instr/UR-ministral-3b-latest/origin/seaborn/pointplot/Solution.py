import seaborn as sns

# Sample data using seaborn's built-in dataset 'tips'
tips = sns.load_dataset("tips")

# Plotting the point estimates and errors with lines and markers
sns.lineplot(x='total_bill', y='tip', data=tips, marker='o')

# Plotting within the same figure to maintain scale
sns.scatterplot(data=tips, x='total_bill', y='tip', alpha=0.4)

