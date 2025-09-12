
import matplotlib.pyplot as plt
import seaborn as sns

# Load the iris dataset
iris = sns.load_dataset("iris")

# Define the variables for the categorical scatterplot
x = "species"
y = "sepal_length"
hue = "species"
data = iris[["sepal_width", "petal_width", "species"]]

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(6, 4))

# Plot the categorical scatterplot with non-overlapping points
sns.scatterplot(x=x, y=y, hue=hue, data=data, ax=ax)

# Adjust the x axis limits to avoid overlap
ax.set_xlim(-0.5, 2.5)

# Add a title and labels to the plot
plt.title("Categorical Scatterplot with Non-Overlapping Points")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Width")

# Show the plot
plt.show()
