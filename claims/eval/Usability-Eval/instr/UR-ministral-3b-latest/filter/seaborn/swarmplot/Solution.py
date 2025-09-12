import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a DataFrame `df` with two columns 'x' and 'y'
df = sns.load_dataset("iris")

sns.catplot(data=df, kind="scatter", x="x", y="y", hue="species", palette="coolwarm")

plt.show()
