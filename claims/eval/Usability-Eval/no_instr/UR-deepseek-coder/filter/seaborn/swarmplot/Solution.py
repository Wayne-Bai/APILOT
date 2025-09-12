import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Value': [1, 2, 3, 4, 5, 6, 7, 8, 9]
}

# Create a DataFrame
df = sns.load_dataset('tips')

# Draw a categorical scatterplot with non-overlapping points
sns.swarmplot(x='day', y='total_bill', data=df)

# Show the plot
plt.show()
