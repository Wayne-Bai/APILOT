# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Create a barplot to show counts of observations in each categorical bin
sns.histplot(tips, x="day", multiple="dodge", shrink=True, stat='count', edgecolor='black')

# Set title and labels
plt.title('Counts of Observations in Each Categorical Bin')
plt.xlabel('Day of the Week')
plt.ylabel('Count of Observations')

# Show the plot
plt.show()
