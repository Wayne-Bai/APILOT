import seaborn as sns
import matplotlib.pyplot as plt

# Load a dataset
tips = sns.load_dataset("tips")

# Create a seaborn plot
plot = sns.lineplot(x="total_bill", y="tip", data=tips)

# Configure the appearance of tick labels for the scale's axis
plot.set_xformat('hd,Dd')  # Set the format for x-axis ticks
plot.set_yformat('hd,Dd')  # Set the format for y-axis ticks

# Configure the appearance of tick labels for the legend
plot.legend.get_texts()[0].set_text('Total Bill: $' + '${:.0f}'.format(tips['total_bill'].mean()))

# Display the plot
plt.show()
