import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [1, 2, 3, 4]

# Create a categorical scatterplot with non-overlapping points
sns.stripplot(x=categories, y=values, jitter=True, dodge=True)

# Show the plot
plt.show()
