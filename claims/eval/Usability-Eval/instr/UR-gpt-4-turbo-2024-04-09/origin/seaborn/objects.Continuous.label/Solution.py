import seaborn as sns
import matplotlib.pyplot as plt

# Load example data
data = sns.load_dataset("iris")

# Create a plot
sns_plot = sns.scatterplot(data=data, x='sepal_length', y='sepal_width', hue='species')

# Configure the appearance of tick labels for the scale's axis
plt.xticks(rotation=45, fontsize=12, color='red')
plt.yticks(rotation=45, fontsize=12, color='blue')

# Show the plot
plt.show()
