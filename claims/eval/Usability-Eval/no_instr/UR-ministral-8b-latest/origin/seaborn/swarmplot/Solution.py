import seaborn as sns
import matplotlib.pyplot as plt

# Sample data for demonstration
data = sns.load_dataset("iris")

# Adjust the size of each point to make them non-overlapping
data["point_size"] = 100  # Point size can be adjusted as needed

# Create a categorical scatter plot
plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(data=data, x="sepal_length", y="sepal_width", hue="species", style="species", size="point_size", s=100)

# Customize the plot (optional)
scatter.set_title("Categorical Scatter Plot with Non-Overlapping Points")
plt.show()
