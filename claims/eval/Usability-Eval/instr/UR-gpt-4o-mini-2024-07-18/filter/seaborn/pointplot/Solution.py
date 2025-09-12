import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Example data
data = {
    'x': ['A', 'B', 'C', 'D'],
    'y': [2, 3, 5, 7],
    'y_err': [0.5, 0.4, 0.6, 0.7]
}

df = pd.DataFrame(data)

# Create a point plot with error bars using line with markers
sns.pointplot(data=df, x='x', y='y', ci=None)  # ci=None to avoid default confidence intervals
plt.errorbar(df['x'], df['y'], yerr=df['y_err'], fmt='o', capsize=5, color='red', label='Error bars')
plt.legend()
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Point Estimates with Error Bars')
plt.show()
