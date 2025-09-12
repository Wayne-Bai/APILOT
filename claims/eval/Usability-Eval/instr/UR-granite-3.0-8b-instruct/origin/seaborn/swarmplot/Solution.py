import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a DataFrame df with columns 'x', 'y', and 'category'
# Replace 'x', 'y', and 'category' with your actual column names

# Create a scatterplot with non-overlapping points
scatter = sns.scatterplot(
    x='x', y='y', hue='category', data=df, palette='viridis'
)

# Adjust the plot to be non-overlapping
for i, point in scatter.collections[0].get_paths():
    vertices = point.vertices
    for j in range(len(vertices) - 1):
        x1, y1 = vertices[j]
        x2, y2 = vertices[j + 1]
        if x1 == x2:  # horizontal line
            y = (y1 + y2) / 2
            vertices[j] = (x1, y)
            vertices[j + 1] = (x2, y)
        elif y1 == y2:  # vertical line
            x = (x1 + x2) / 2
            vertices[j] = (x, y1)
            vertices[j + 1] = (x, y2)

plt.show()
