import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [4, 7, 1, 8]
}
df = pd.DataFrame(data)

# Create a function to draw bar chart for DataFrame background
def bar_chart_background(data):
    default_height = 0.5
    max_value = data['Values'].max()
    
    # Create a figure for the bar chart
    fig, ax = plt.subplots(figsize=(6, len(data) * default_height))
    
    # Draw bars
    ax.barh(data['Category'], data['Values'], color='skyblue')
    
    ax.set_xlim(0, max_value + 1)
    ax.axis('off')  # Hide the axes
    
    # Render the bar chart on a background
    plt.show()

# Call the function with the DataFrame
bar_chart_background(df)
