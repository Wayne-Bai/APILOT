import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample data creation
np.random.seed(0)
data = pd.DataFrame({
    'x': np.arange(10),
    'y': np.random.rand(10) * 10,
    'error': np.random.rand(10)
})

# Point estimates with error bars
sns.lineplot(data=data, x='x', y='y', marker='o', ci=None)  # `ci=None` to not show confidence intervals
plt.errorbar(data['x'], data['y'], yerr=data['error'], fmt='o', capsize=5, color='orange', label='Error bars')
plt.title('Point Estimates with Error Bars')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
