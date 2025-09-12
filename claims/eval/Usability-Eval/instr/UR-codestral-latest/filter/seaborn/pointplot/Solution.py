import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Assuming we have some data for demonstration
np.random.seed(0)
data = np.random.normal(0, 1, 1000)

# Create a simple line plot with errors represented as shaded areas
plot = sns.lineplot(x=np.arange(len(data)), y=data, marker="o")

# Add error bars (standard deviation)
std_dev = np.std(data)
error_bars = plt.fill_between(np.arange(len(data)), (data - std_dev), (data + std_dev), alpha=0.2)

plt.show()
