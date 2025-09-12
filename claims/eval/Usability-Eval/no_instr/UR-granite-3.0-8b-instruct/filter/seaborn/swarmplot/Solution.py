import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a DataFrame df with columns 'x', 'y', and 'cat'
# where 'x' and 'y' are the coordinates and 'cat' is the categorical variable

# Create a scatterplot with non-overlapping points
sns.scatterplot(x='x', y='y', hue='cat', data=df, s=100)

# Show the plot
plt.show()
