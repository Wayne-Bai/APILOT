# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample DataFrame
np.random.seed(0)
data = np.random.randint(1, 100, size=(5, 5))
df = pd.DataFrame(data, columns=list('ABCDE'))

# Define a function to draw bar chart in cell backgrounds
def draw_bars(df):
    # Create a figure and axis object
    fig, ax = plt.subplots(figsize=(10, 6))

    # Hide axes
    ax.axis('off')

    # Iterate over each cell in the DataFrame
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            # Get the value of the current cell
            value = df.iloc[i, j]

            # Calculate the width of the bar
            width = value / df.values.max() * 0.8

            # Create a bar
            ax.add_patch(plt.Rectangle((j, i), width, 0.8, color='blue', alpha=0.5))

            # Add text to the cell
            ax.text(j + 0.5, i + 0.4, str(value), ha='center', va='center')

    # Set the limits of the axes
    ax.set_xlim(0, df.shape[1])
    ax.set_ylim(0, df.shape[0])

    # Set the ticks of the axes
    ax.set_xticks(range(df.shape[1]))
    ax.set_yticks(range(df.shape[0]))

    # Set the tick labels of the axes
    ax.set_xticklabels(df.columns)
    ax.set_yticklabels(df.index)

# Draw the bar chart in the cell backgrounds
draw_bars(df)

# Show the plot
plt.show()
