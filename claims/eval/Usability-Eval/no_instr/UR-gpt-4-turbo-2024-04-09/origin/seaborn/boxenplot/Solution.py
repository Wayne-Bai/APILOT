import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample larger dataset
data = sns.load_dataset('diamonds')  # Using the diamonds dataset as an example of a larger dataset

# Draw an enhanced box plot
plt.figure(figsize=(12, 6))
sns.boxplot(x='carat', y='price', data=data)
plt.title('Enhanced Box Plot for Larger Dataset')
plt.show()
