import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a DataFrame df with columns 'x' and 'y'
# Replace 'x' and 'y' with your actual column names
sns.kdeplot(df['x'], df['y'], shade=True, cmap='Blue')

# To add observations or box plot statistics, you can use the following code:
# For observations
plt.scatter(df['x'], df['y'], color='red')

# For box plot statistics
sns.boxplot(x='x', y='y', data=df, whis=[5, 95])

plt.show()
