import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create some example data
np.random.seed(0)
data = np.random.normal(size=1000)

# Create a kde (Kernel Density Estimate) patch
kde = sns.kdeplot(data, shade=True, fill=False)

# Add observations and box plot statistics on the kde
sns.kdeplot(data, cmap="Set2")

# Calculate and add box plot statistics
stats = sns.boxplot(data=[data])

# Show the plot
plt.show()
