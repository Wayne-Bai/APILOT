# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the exampleTips dataset
tips = sns.load_dataset("tips")

# Create a count plot
plt.figure(figsize=(10,6))
sns.countplot(x="day", hue="sex", data=tips)

# Add title and labels
plt.title('Counts of observations in each categorical bin')
plt.xlabel('Day of the week')
plt.ylabel('Count')

# Show the plot
plt.show()
