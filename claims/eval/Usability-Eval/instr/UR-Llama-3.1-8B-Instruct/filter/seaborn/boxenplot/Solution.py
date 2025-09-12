# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
tips = sns.load_dataset("tips")

# Draw an enhanced box plot using 'boxplot' function with'ومع showfliers=False'
plt.figure(figsize=(8,6))
sns.boxplot(data=tips, showfliers=False)

# Set the title and labels
plt.title('Enhanced Box Plot for Larger Datasets')
plt.xlabel('Day')
plt.ylabel('Total Bill')

# Show the plot
plt.show()
