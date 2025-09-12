import pandas as pd
import matplotlib.pyplot as plt

# Assuming df is your DataFrame
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [10, 20, 15, 30, 25]
})

# Draw bar chart
plt.bar(df['Category'], df['Value'])
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
