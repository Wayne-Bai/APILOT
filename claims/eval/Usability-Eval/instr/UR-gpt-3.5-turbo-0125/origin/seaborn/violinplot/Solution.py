
import seaborn as sns
import matplotlib.pyplot as plt

# Create some sample data
data = sns.load_dataset('iris')

# Create a KDE plot with box plot statistics overlaid
sns.violinplot(x='species', y='sepal_length', data=data, inner='quartile')

# Display the plot
plt.show()
