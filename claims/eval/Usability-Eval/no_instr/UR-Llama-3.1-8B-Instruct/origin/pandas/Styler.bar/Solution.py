# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [10, 15, 7, 12, 20]
}
df = pd.DataFrame(data)

# Set the Category as the index
df.set_index('Category', inplace=True)

# Draw the bar chart
plt.figure(figsize=(8, 6))
df.plot(kind='bar', rot=0, colormap='viridis')

# Add a grid and title
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.title('Bar Chart in DataFrame Cell Background')

# Show the plot
plt.show()
