import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset("titanic")  # Example dataset

# Create a count plot
sns.countplot(x='class', data=data)

# Show the plot
plt.title('Count of Observations in Each Categorical Bin')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()
