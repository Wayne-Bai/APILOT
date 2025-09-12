import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset('iris')

# Create the KDE plot
sns.kdeplot(data=data, x='sepal_length', fill=True, color='blue', alpha=0.5)

# Overlay a box plot
sns.boxplot(data=data, x='sepal_length', color='orange', width=0.2)

# Show the plot
plt.title('KDE with Box Plot Statistics')
plt.xlabel('Sepal Length')
plt.ylabel('Density')
plt.show()
