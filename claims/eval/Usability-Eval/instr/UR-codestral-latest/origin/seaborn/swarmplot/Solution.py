import seaborn as sns
import matplotlib.pyplot as plt

# Assume we have a DataFrame `df` with columns 'category' and 'value'

# Draw a categorical scatterplot with points adjusted to be non-overlapping
sns.stripplot(x="category", y="value", data=df, jitter=True)

# Display the plot
plt.show()
