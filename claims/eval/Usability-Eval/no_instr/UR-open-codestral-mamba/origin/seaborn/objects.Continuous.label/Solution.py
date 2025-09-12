import seaborn as sns
import matplotlib.pyplot as plt

# Set the background style of the plot
sns.set(style='whitegrid')

# Load the example tips dataset
tips = sns.load_dataset('tips')

# Create a simple bar plot
plot = sns.barplot(x='day', y='total_bill', data=tips)

# Add tick labels to the x-axis
plot.set_xticklabels(['Sunday', 'Monday', 'Tuesday', 'Wednesday'], rotation=45)

# Display the plot
plt.show()
