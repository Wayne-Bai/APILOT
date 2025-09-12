import pandas as pd

# Sample DataFrame
data = {'Category': ['A', 'B', 'C', 'D'],
        'Values': [10, 20, 30, 40]}

df = pd.DataFrame(data)

# Set up the figure and axis
import matplotlib.pyplot as plt

# Create bar chart
ax = df.plot(kind='bar', x='Category', y='Values', legend=True)

# Draw borders to the background
fig = ax.figure
ax.set_facecolor('white')

# Show the plot
plt.show()
