import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample dataset
tips = sns.load_dataset("tips")

# Create a bar plot
ax = sns.barplot(x="day", y="total_bill", data=tips)

# Configure the appearance of tick labels for the x-axis
ax.set_xticklabels(['Thurs', 'Fri', 'Sat', 'Sun'], rotation=45)

# Configure the appearance of tick labels for the y-axis
ax.set_yticklabels(['$0', '$20', '$40', '$60', '$80', '$100'] + ax.get_yticks()[5:])

# Show the plot
plt.show()
