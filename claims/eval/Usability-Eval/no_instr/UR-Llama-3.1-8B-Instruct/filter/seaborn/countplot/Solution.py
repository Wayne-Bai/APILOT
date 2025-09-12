# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the example tips dataset
tips = sns.load_dataset('tips')

# Print the first few rows of the dataset
print(tips.head())

# Plot the counts of observations in each categorical bin using bars
sns.countplot(x='day', data=tips)

# Show the counts above each bar
plt.show()
