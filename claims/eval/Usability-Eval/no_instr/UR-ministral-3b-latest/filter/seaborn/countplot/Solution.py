import seaborn as sns
import matplotlib.pyplot as plt

# Assuming we have a DataFrame `df` with a categorical column named 'category'
# Generate a bar plot of the counts of observations in each category
sns.countplot(data=df, x='category')
plt.show()
