import seaborn as sns

# Create a dataset
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Draw a patch representing a KDE
sns.kdeplot(data, shade=True)

# Add observations or box plot statistics
sns.boxplot(data)
