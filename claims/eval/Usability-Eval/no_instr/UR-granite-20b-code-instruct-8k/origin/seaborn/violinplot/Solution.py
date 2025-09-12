import seaborn as sns

# Load example tips dataset
tips = sns.load_dataset("tips")

# Draw a KDE plot with seaborn
sns.kdeplot(tips["total_bill"])

# Add observations to the plot
sns.violinplot(x="day", y="total_bill", data=tips)

# Add box plot statistics to the plot
sns.boxplot(x="day", y="total_bill", data=tips)
