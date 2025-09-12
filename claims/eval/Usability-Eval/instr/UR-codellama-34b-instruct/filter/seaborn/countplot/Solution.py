
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Generate some sample data
data = pd.DataFrame({'category': ['A', 'B', 'C'],
                    'count': [10, 20, 30]})

# Use seaborn to create a bar plot showing the counts of observations in each categorical bin
sns.barplot(x='category', y='count', data=data)

# Customize the plot as needed
plt.title("Counts by Categorical Bin")
plt.xlabel("Category")
plt.ylabel("Count")

# Show the plot
plt.show()
