
import seaborn as sns
import matplotlib.pyplot as plt

# Create an example dataset
data = sns.load_dataset("iris")

# Plot with point estimates and error bars
sns.pointplot(x="species", y="sepal_length", data=data)

# Show the plot
plt.show()
