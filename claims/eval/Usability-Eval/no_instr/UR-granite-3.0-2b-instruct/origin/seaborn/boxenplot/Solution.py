# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (replace 'dataset.csv' with your actual dataset)
df = sns.load_dataset('dataset.csv')

# Create an enhanced box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='column_name', y='column_name')

# Add title and labels
plt.title('Enhanced Box Plot for Larger Datasets')
plt.xlabel('Column Name')
plt.ylabel('Value')

# Show the plot
plt.show()
