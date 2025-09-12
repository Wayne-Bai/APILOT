import seaborn as sns

# Assuming you have a DataFrame called 'data' with a categorical column called 'category'
sns.countplot(x='category', data=data)
