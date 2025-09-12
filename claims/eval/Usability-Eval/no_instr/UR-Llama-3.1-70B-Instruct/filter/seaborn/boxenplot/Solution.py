# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate a large dataset
np.random.seed(0)
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(1, 1.5, 1000)

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(8, 6))

# Create a boxplot with seaborn
sns.boxplot(data=[data1, data2], ax=ax)

# Customize the plot
ax.set_title("Enhanced Box Plot for Larger Datasets")
ax.set_xlabel("Dataset")
ax.set_ylabel("Value")

# Show the plot
plt.show()

# Alternatively, using a tips dataset
tips = sns.load_dataset("tips")

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(8, 6))

# Create a boxplot with seaborn, using hue for more information
sns.boxplot(x="day", y="total_bill", hue="sex", data=tips, ax=ax)

# Customize the plot
ax.set_title("Total Bill by Day and Sex")
ax.set_xlabel("Day")
ax.set_ylabel("Total Bill")

# Show the plot
plt.show()
