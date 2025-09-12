import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = sns.load_dataset('tips')

# Map each category to a unique color
unique_colors = np.random.choice(range(10), size=len(data['day']), replace=False)

# Create a scatter plot with non-overlapping points
sns.scatterplot(data=data, x='total_bill', y='tip', hue='day', palette=unique_colors, legend=False)

# Label the axes
plt.xlabel('Total Bill')
plt.ylabel('Tip')

# Show the plot
plt.show()
