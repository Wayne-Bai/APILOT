import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Assuming you have a DataFrame 'df' with a column 'data'
kde = gaussian_kde(df['data'])

# Create a grid of x and y values
x = np.linspace(df['data'].min(), df['data'].max(), 100)
y = kde(x)

# Plot the KDE
plt.plot(x, y)
plt.fill_between(x, y, alpha=0.2, color='blue')

# Add observations or box plot statistics
plt.scatter(df['data'], [0] * len(df['data']), color='red', label='Observations')
plt.boxplot(df['data'], vert=False, showmeans=True, meanline=True, whis=[5, 95], labels=['Data'])

plt.legend()
plt.show()
