import seaborn as sns

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a barplot
bar = sns.barplot(x="day", y="total_bill", data=tips, ci="sd")

# Show the plot
sns.plt.show()
