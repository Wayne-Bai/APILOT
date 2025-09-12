import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B', 'A'],
    'Value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}

# Create a DataFrame
df = sns.load_dataset('tips')  # Replace with your actual data

# Plot the counts of observations in each categorical bin using bars
sns.countplot(x='Category', data=df)

# Show the plot
plt.show()
