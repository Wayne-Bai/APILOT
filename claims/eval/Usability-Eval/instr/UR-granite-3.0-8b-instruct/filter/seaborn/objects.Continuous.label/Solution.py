import seaborn as sns
import matplotlib.pyplot as plt

# Create a simple line plot
tips = sns.load_dataset("tips")
plot = sns.relplot(x="total_bill", y="tip", data=tips)

# Configure the appearance of tick labels for the x-axis
plot.axes[0,0].xaxis.set_major_formatter(sns.axes_style()["xaxis.major.formatter"])
plot.axes[0,0].xaxis.set_major_locator(plt.MultipleLocator(50))

# Configure the appearance of tick labels for the y-axis
plot.axes[0,0].yaxis.set_major_formatter(sns.axes_style()["yaxis.major.formatter"])
plot.axes[0,0].yaxis.set_major_locator(plt.MultipleLocator(10))

# Configure the appearance of tick labels for the legend
plot.legend().set_title("Legend")

plt.show()
