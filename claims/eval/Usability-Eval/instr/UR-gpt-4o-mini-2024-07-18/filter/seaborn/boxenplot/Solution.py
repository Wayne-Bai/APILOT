import seaborn as sns
import matplotlib.pyplot as plt

# Generate a large dataset for demonstration
import numpy as np
data = np.random.normal(size=1000)

# Create an enhanced box plot
plt.figure(figsize=(12, 6))
sns.boxplot(data=data, color='lightblue', fliersize=5)

# Enhance with additional features
plt.title('Enhanced Box Plot for Larger Datasets', fontsize=16)
plt.xlabel('Data', fontsize=14)
plt.grid(True)

# Show the plot
plt.show()
