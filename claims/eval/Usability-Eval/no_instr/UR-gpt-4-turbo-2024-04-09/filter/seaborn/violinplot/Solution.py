import seaborn as sns
import matplotlib.pyplot as plt

# Load a dataset
data = sns.load_dataset("iris")

# Draw a KDE plot with observations
sns.kdeplot(data=data['sepal_width'], fill=True)
sns.scatterplot(data=data, x=range(len(data)), y='sepal_width', color='r')

# Alternatively, draw a box plot with overlaid scatter plot for observations
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, y='sepal_length', color='lightblue')
sns.stripplot(data=data, y='sepal_length', color='red', size=4, jitter=True)

plt.show()
