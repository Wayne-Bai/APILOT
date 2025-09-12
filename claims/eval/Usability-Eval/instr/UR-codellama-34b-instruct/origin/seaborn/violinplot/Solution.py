import seaborn as sns
import matplotlib.pyplot as plt

# Generate some sample data
x = np.random.normal(0, 1, size=100)
y = np.random.normal(0, 1, size=100)
data = pd.DataFrame({'x': x, 'y': y})

# Create a KDE plot of the data
sns.kdeplot(data['x'], data['y'], shade=True, cmap='Blues')

# Add observations or box plot statistics to the plot
sns.boxplot(x='x', y='y', data=data)
plt.legend()
