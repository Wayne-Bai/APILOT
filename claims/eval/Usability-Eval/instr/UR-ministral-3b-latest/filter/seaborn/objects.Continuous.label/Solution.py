import seaborn as sns
import matplotlib.pyplot as plt

# Create a simple dataset using seaborn's built-in dataset
df = sns.load_dataset('iris')

# Create a plot
sns.set(style="whitegrid")
ax = sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species')

# Custom tick labels on x-axis
x_ticks = ['5cm', '6cm', '7cm']
ax.set_xticks([5, 6, 7])

# Custom tick labels on legend
legend_labels = [i.upper() for i in ax.legend().get_texts()]
ax.legend(legend_labels)
