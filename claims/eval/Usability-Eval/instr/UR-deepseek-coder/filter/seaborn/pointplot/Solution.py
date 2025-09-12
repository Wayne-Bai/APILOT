import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Mean': [23, 30, 21, 28],
    'Error': [2, 3, 2.5, 3.5]
}

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Plotting
sns.pointplot(x='Category', y='Mean', data=df, markers='o', linestyles='-', ci='Error')

# Show the plot
plt.show()
