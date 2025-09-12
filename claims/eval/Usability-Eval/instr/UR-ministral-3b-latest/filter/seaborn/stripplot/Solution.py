import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Category': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C'],
    'Value': [1, 2, 3, 4, 5, 6, 7, 8]
}

# Create a DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Draw the strip plot
sns.stripplot(x='Category', y='Value', data=df, jitter=True)

# Show the plot
plt.show()
