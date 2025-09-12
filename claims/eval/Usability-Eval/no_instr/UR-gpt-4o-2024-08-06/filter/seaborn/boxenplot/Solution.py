import seaborn as sns
import matplotlib.pyplot as plt

# Sample data for demonstration
data = sns.load_dataset('diamonds')

# Enhanced box plot with seaborn
plt.figure(figsize=(12, 8))  # Adjust figure size for better visibility

# Creating an enhanced box plot
# Here we add jitter to the data points to visualize data distribution better
sns.boxplot(x='cut', y='price', data=data, whis=1.5, fliersize=0)
sns.stripplot(x='cut', y='price', data=data, jitter=True, color='royalblue', alpha=0.3)

# Adding a title and labels
plt.title('Enhanced Box Plot of Diamond Prices by Cut', fontsize=16)
plt.xlabel('Cut', fontsize=14)
plt.ylabel('Price', fontsize=14)

plt.show()
