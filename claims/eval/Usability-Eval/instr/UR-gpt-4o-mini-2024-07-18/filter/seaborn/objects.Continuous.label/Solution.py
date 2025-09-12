import seaborn as sns
import matplotlib.pyplot as plt

# Example data
data = sns.load_dataset("iris")

# Create a basic scatter plot
sns.scatterplot(data=data, x="sepal_length", y="sepal_width", hue="species")

# Configure the appearance of tick labels
plt.xticks(rotation=45, fontsize=10, fontweight='bold')
plt.yticks(fontsize=10, fontweight='bold')

# Show the plot
plt.show()
