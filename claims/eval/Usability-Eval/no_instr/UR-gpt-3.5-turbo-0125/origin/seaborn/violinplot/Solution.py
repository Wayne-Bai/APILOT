
import seaborn as sns
import matplotlib.pyplot as plt

# Create data
data = sns.load_dataset("diamonds")

# Create a violin plot and combine with box plot statistics
ax = sns.violinplot(x="cut", y="price", data=data)
sns.boxplot(x="cut", y="price", data=data, ax=ax, width=0.2, linewidth=2.5)

plt.show()
