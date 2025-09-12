import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Assume we have some data
tips = sns.load_dataset("tips")

# Add some jitter to the x positions
tips['total_bill'] = tips['total_bill'] + np.random.rand(len(tips['total_bill'])) - 0.5

# Create the plot
plt.figure(figsize=(8,6))
sns.stripplot(x='day', y='total_bill', data=tips, jitter=False)
plt.title('Scatterplot of Tip Total by Day')
plt.show()
