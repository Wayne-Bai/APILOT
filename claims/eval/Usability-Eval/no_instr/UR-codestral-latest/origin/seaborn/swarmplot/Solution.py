import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Your data
# Replace the following lines with your actual data
x = np.random.randint(0, 4, 100)
y = np.random.randn(100)

# Add some randomness to the x values
x = x + np.random.normal(0, 0.05, len(x))

# Create the scatterplot
sns.stripplot(x=x, y=y)

# Display the plot
plt.show()
