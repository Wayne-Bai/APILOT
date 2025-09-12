
import seaborn as sns

# Load the iris dataset
iris = sns.load_dataset("iris")

# Draw a categorical scatterplot with points adjusted to be non-overlapping
sns.scatterplot(x="petal_length", y="sepal_width", data=iris, hue="species", alpha=0.5)
