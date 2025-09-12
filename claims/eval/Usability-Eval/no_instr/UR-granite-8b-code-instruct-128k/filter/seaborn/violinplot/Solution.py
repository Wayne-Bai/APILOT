import seaborn as sns

# Create a patch representing a KDE and add observations or box plot statistics
sns.kdeplot(data, shade=True)
sns.boxplot(data)