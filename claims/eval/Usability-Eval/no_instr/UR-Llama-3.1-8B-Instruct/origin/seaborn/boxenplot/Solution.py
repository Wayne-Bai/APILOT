# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Generate a large dataset for demonstration
np.random.seed(0)
data = np.random.randn(1000)

# Load the dataset
tips = sns.load_dataset("tips")

# Create an enhanced box plot for the dataset
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(data=[data], ax=ax)

# Add a title to the plot
ax.set_title('Enhanced Box Plot for Larger Datasets')

# Display the plot
plt.show()

# Enhanced Box plot for the 'total_bill' column in the 'tips' dataset
plt.figure(figsize=(8, 6))
sns.boxplot(x="total_bill", data=tips, showmeans=True, meanline=True, boxprops=dict(alpha=0.5), medianprops=dict(color="red"), whiskerprops=dict(color="green"), showcaps=True, showfliers=True)

# Add a title to the plot
plt.title('Enhanced Box Plot for "total_bill" in Tips Dataset')

# Display the plot
plt.show()

# Enhanced Box plot with histograms on the sides for the 'total_bill' column in the 'tips' dataset
plt.figure(figsize=(8, 6))
sns.boxplot(x="total_bill", data=tips, showmeans=True, meanline=True, boxprops=dict(alpha=0.5), medianprops=dict(color="red"), whiskerprops=dict(color="green"), showcaps=True, showfliers=True)
sns.boxplot(x="total_bill", data=tips, showmeans=True, meanline=True, boxprops=dict(alpha=0.5), medianprops=dict(color="red"), whiskerprops=dict(color="green"), showcaps=True, showfliers=False, orient="s")

# Add a title to the plot
plt.title('Enhanced Box Plot with Histograms on the Sides for "total_bill" in Tips Dataset')

# Display the plot
plt.show()
