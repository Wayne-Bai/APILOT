import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [2, 3, 5, 7, 11],
    'error': [0.5, 0.7, 1.0, 1.2, 1.5]
}

# Create a DataFrame
df = sns.load_dataset('tips')

# Plotting
sns.lineplot(x='total_bill', y='tip', data=df, marker='o', err_style='bars', ci='sd')

# Show the plot
plt.show()
