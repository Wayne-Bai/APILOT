import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample data creation
np.random.seed(10)
x = np.linspace(0, 10, 30)
y = np.sin(x) + np.random.normal(size=x.size) * 0.5

# Creating DataFrame
data = pd.DataFrame({'x': x, 'y': y})

# Creating the plot
sns.set(style="whitegrid")

# Use seaborn's 'lineplot' for line with markers and error bands
sns.lineplot(x='x', y='y', data=data, marker='o', ci='sd')

plt.title('Line plot with point estimates and error bands')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
