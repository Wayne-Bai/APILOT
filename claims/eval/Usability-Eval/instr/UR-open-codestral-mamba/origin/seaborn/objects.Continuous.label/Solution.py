import seaborn as sns
import matplotlib.pyplot as plt

# Set style of the plot
sns.set(style="whitegrid")

# Make some sample data for the plot
tips = sns.load_dataset("tips")

# Create a plot with a boxplot and a scatterplot on the same axes
fig, ax = plt.subplots()

sns.boxplot(x="total_bill", y="day", data=tips, orient="h", ax=ax)
sns.swarmplot(x="total_bill", y="day", data=ticks, orient="h", color=".25", ax=ax)

# Set the appearance of tick labels
ax.tick_params(axis='y', labelsize=12)
ax.tick_params(axis='x', labelsize=12)

plt.show()
