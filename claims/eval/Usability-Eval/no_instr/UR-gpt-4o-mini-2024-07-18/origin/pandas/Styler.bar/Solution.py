import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {'Category': ['A', 'B', 'C', 'D'],
        'Values': [4, 7, 1, 8]}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting the bar chart
plt.figure(figsize=(8, 4))
plt.bar(df['Category'], df['Values'], color='lightblue')
plt.title('Bar Chart in Cell Backgrounds')
plt.xlabel('Category')
plt.ylabel('Values')
plt.grid(axis='y')

# Show the plot
plt.show()
