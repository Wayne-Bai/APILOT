import seaborn as sns
import matplotlib.pyplot as plt

# Example data: Generating a larger dataset
data = sns.load_dataset("diamonds")

# Enhanced box plot
plt.figure(figsize=(12, 6))
sns.boxplot(x='cut', y='price', data=data, palette='Set2', showfliers=False)

# Adding a jitter on top of the boxplot for better visualization of the data distribution
sns.swarmplot(x='cut', y='price', data=data, color='black', alpha=0.5, size=3)

# Enhancing the plot with title and labels
plt.title('Enhanced Box Plot of Diamond Prices by Cut', fontsize=16)
plt.xlabel('Cut', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.grid(True)

plt.show()
