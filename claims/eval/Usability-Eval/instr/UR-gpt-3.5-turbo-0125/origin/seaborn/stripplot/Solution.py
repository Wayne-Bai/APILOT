
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample dataframe (replace this with your actual data)
data = {'Category': ['A'] * 100 + ['B'] * 100 + ['C'] * 100,
        'Values': np.random.randn(300)}

# Create a categorical scatterplot with jitter
sns.stripplot(x='Category', y='Values', data=data, jitter=True)

# Show the plot
plt.show()
