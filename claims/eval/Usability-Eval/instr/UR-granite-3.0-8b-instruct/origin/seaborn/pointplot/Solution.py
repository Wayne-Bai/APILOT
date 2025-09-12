import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sample data
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = np.sin(x)
y_err = 0.1 * np.abs(np.random.normal(size=100))

# Create a point plot with error bars
plt.figure(figsize=(8, 6))
sns.pointplot(x, y, markers='o', errwidth=2, capsize=5, yerr=y_err)
plt.title('Point Estimates and Errors using Lines with Markers')
plt.show()
