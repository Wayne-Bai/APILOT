# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Randomly generate data
np.random.seed(0)
x = np.random.choice(['A', 'B', 'C'], 50)
y = np.random.choice(['D', 'E', 'F'], 50)
size = np.random.rand(50)*100
color = np.random.rand(50)
category_x = ['A']*25 + ['B']*25
category_y = ['D']*25 + ['E']*25

# Create a new figure
plt.figure(figsize=(8,6))

# Draw the categorical scatterplot with points adjusted to be non-overlapping
tips = pd.DataFrame({
    'x': x,
    'y': y,
   'size': size,
    'color': color,
    'category_x': category_x,
    'category_y': category_y
})

plot = sns.scatterplot(
    data=tips,
    x='x',
    y='y',
    hue='category_x',
    palette=' Spectral',
    size='size',
    sizes=(10, 500),
    markers=['o']*25 + ['s']*25,
    hue_order = ['A', 'B'],
    s=100,
    linewidth=0,
    legend=False,
)

# Set the limit for x and y axes
plt.xlim([0, 7])
plt.ylim([0, 9])

# Set title and labels
plt.title('Categorical Scatterplot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()
