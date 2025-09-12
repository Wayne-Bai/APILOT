import seaborn as sns
import matplotlib.pyplot as plt

# Load a dataset from seaborn
titanic = sns.load_dataset("titanic")

# Create a boxplot
sns.boxplot(x="class", y="fare", data=titanic)

# Get the current axis
ax = plt.gca()

# Set the font size of x and y tick labels
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)

# Set the rotation of x tick labels
plt.setp(ax.get_xticklabels(), rotation=45)

plt.show()
