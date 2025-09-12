
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generating a large dataset
np.random.seed(10)
data = np.random.normal(loc=0, scale=1, size=(1000, 5))

# Creating an enhanced box plot
plt.figure(figsize=(12, 8))
sns.boxplot(data=data, orient='h', palette='Set2')
plt.xlabel('Value')
plt.title('Enhanced Box Plot for Larger Datasets')
plt.show()
