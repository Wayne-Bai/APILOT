import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset("iris")

# Plotting the KDE
sns.kdeplot(data={"s", "sepal_length", "sepal_width"}, fill=True)

# Adding observations or box plot statistics on the same graph
sns.boxplot(data={"s", "sepal_height"})  # Added here to show mean and outliers

# Showing the plot
plt.show()
