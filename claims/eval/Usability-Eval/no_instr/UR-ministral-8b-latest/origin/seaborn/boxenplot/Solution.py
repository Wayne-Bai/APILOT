import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a DataFrame `df` with a 'column_name' and a 'another_column_name'
# Replace 'column_name' with your actual column name
# Replace 'another_column_name' with your actual column name
data = [df['column_name'], df['another_column_name']]

# Let's create a pairplot with the seaborn library
# Using "box" or "boxen" option to create a box plot
pairplot_data = sns.pairplot(data, hue='column_x')

# Show the plot
plt.show()
