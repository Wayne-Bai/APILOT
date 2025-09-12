import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Generate example data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [12, 15, 6, 14, 18, 13, 17, 16, 19, 10, 8, 11, 9, 12, 23, 24, 25, 27, 32, 28, 29, 21, 19, 22, 24, 30, 26]
}

df = pd.DataFrame(data)

# Create the box plot
sns.boxplot(x='Category', y='Values', data=df)

# Display the plot with enhanced aesthetics
plt.title('Enhanced Box Plot for Larger Datasets')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()
