# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy import integrate

# Generate a sample dataset
np.random.seed(0)
x = np.random.randn(100)

# Plot the KDE
plt.figure(figsize=(8,6))
sns.kdeplot(x, shade=True, label='KDE')

# Add the observations as bars on top of the KDE
plt.hist(x, bins=10, density=True, alpha=0.6, label='Observations', histtype='bar', width=0.8)

# Add box plot statistics
sns.boxplot(x, showmeans=True, boxprops={'facecolor':'none'}, showfliers=False, meansize=8)

# Add labels and title
plt.title('KDE with Observations and Box Plot Statistics')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()

# Display the plot
plt.show()
