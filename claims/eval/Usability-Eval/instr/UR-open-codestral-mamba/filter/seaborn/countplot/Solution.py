import seaborn as sns
import matplotlib.pyplot as plt

# Example data, replace it with your own data and adjust the column name
df = sns.load_dataset('tips')

# Create a bar plot
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='day')

# Show the plot
plt.show()
