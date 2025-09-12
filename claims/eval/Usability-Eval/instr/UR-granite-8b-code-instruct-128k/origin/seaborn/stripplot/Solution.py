import seaborn as sns

# Load the dataset
df = sns.load_dataset("iris")

# Draw the scatterplot with jitter
sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=df, jitter=True)
