import pandas as pd
import matplotlib.pyplot as plt

# Creating a simple DataFrame
data = {'Category': ['A', 'B', 'C', 'D', 'E'],
        'Value': [10, 15, 8, 17, 12]}
df = pd.DataFrame(data)

# Plotting the bar chart
plt.figure(figsize=(10,5))
df.set_index('Category')['Value'].plot(kind='bar', color='skyblue')
plt.title('Bar Chart from DataFrame')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
