
import seaborn as sns

# Create a figure object
fig = plt.figure(figsize=(5, 4))

# Generate some random data
data = np.random.randn(100)

# Create a bar chart with Seaborn
sns.barplot(x=range(len(data)), y=data, orient='h')

# Set the tick labels for the x-axis
sns.set_xticklabels(rotation=45)

# Add a custom tick label
ticks = np.linspace(0, 100, 5)
tick_labels = [f"{x:.2f}" for x in ticks]
sns.axes.set_xticklabels(ticks=ticks, labels=tick_labels)

# Set the tick labels for the y-axis
sns.set_yticklabels(rotation=45)

# Add a custom tick label
ticks = np.linspace(0, 100, 5)
tick_labels = [f"{x:.2f}" for x in ticks]
sns.axes.set_yticklabels(ticks=ticks, labels=tick_labels)

# Set the tick label font size
sns.set_xticklabel_fontsize(10)
sns.set_yticklabel_fontsize(10)
