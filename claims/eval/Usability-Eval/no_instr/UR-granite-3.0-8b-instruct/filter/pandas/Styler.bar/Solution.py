import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assuming you have a DataFrame 'df' with columns 'Category' and 'Value'
# Create a sample DataFrame
data = {'Category': ['A', 'B', 'C', 'D', 'E'],
        'Value': [10, 20, 15, 30, 25]}
df = pd.DataFrame(data)

# Create a bar chart
plt.bar(df['Category'], df['Value'])
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
