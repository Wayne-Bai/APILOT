
import seaborn as sns
import matplotlib.pyplot as plt

# Generate the data to plot (assuming data is in variable 'data' with categorical values in a column 'category')
data = pd.DataFrame({'category': ['A', 'A', 'B', 'A', 'B', 'C', 'C', 'C', 'C']})

# Create countplot
plt.figure(figsize=(8, 6))
sns.countplot(x='category', data=data)

# Show the plot
plt.show()
