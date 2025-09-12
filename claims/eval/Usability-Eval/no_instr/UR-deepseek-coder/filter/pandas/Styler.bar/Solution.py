import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [3, 7, 1, 5]
}
df = pd.DataFrame(data)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the bar chart
df.plot(kind='bar', x='Category', y='Value', ax=ax, legend=False)

# Set the background color of the bars
for i, bar in enumerate(ax.patches):
    bar.set_facecolor(plt.cm.viridis(df['Value'][i] / df['Value'].max()))

# Display the plot
plt.show()
