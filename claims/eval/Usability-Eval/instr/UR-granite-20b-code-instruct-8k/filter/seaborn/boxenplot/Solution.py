import seaborn as sns

# Generate an example dataset
data = sns.load_dataset('tips')

# Create an enhanced box plot
sns.boxplot(x="day", y="total_bill", data=data)
