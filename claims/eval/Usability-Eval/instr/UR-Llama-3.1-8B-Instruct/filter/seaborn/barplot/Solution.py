import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
np.random.seed(0)
x = np.random.randn(10)
y = np.random.randn(10)

# Use the sns.barplot function to create a bar plot with confidence intervals
plt.figure(figsize=(8,6))
sns.barplot(x=x, y=y, capsize=0.2, errbar='ci')

# Set the title and labels
plt.title('Point Estimates and Errors as Rectangular Bars')
plt.xlabel('X-values')
plt.ylabel('Y-values')

# Show the plot
plt.show()
