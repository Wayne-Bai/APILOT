import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample Data
data = {
    'Category': ['A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A'],
    'Values': [12, 20, 35, 25, 30, 20, 25, 15, 27, 18, 30, 35, 20, 22, 32, 16, 24, 14, 40, 21]
}
df = pd.DataFrame(data)

# Sort Data
df.sort_values('Category', inplace=True)

# Plot
plt.figure(figsize=(12, 6))
boxplot = sns.boxplot(x='Category', y='Values', data=df, palette='muted', notch=True, ci=None, yay=True)

# Add title and labels
plt.title('Enhanced Box Plot')
plt.xlabel('Category')
plt.ylabel('Values')

# Display the plot
plt.show()
