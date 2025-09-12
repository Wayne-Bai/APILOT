# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(10,6))

# Draw a categorical scatterplot with jitter
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True, ax=ax)

# Set title and labels
ax.set_title('Categorical Scatterplot with Jitter')
ax.set_xlabel('Day')
ax.set_ylabel('Total Bill')

# Show the plot
plt.show()
