import seaborn as sns
import matplotlib.pyplot as plt

# Example dataset
data = sns.load_dataset("iris")

# Create a KDE plot
plt.figure(figsize=(10, 6))
sns.kdeplot(data=data, x="sepal_length", hue="species", fill=True, common_norm=False, alpha=0.5)

# Add observations as a box plot
sns.boxplot(data=data, x="species", y="sepal_length", whis=[0, 100], width=0.2, palette="dark", fliersize=0)

# Adjust the plot
plt.title('KDE with Box Plot Overlay on Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Density / Observations')
plt.show()
