# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the example tips dataset
tips = sns.load_dataset('tips')

# Show the counts of observations in each categorical bin using bars
plt.figure(figsize=(8,6))
sns.countplot(x='day', data=tips)

# Set the title and labels
plt.title('Counts of Observations by Day')
plt.xlabel('Day')
plt.ylabel('Count')

# Show the plot
plt.show()
