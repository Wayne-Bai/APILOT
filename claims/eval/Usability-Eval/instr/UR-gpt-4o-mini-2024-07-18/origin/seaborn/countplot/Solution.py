import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset("titanic")

# Create a count plot for the 'class' column
sns.histplot(data=data, x='class', discrete=True)

# Show the plot
plt.show()
