import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('data.csv')

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the data using seaborn's lineplot function
sns.lineplot(x='year', y='value', data=df, marker='o', err_style='bar', err_kws={'ecolor': 'black', 'lw': 2})

# Add a title and labels to the plot
ax.set_title('Point Estimates and Errors')
ax.set_xlabel('Year')
ax.set_ylabel('Value')

# Show the plot
plt.show()
