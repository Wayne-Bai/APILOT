
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a dataframe called 'df' with the necessary data
df = pd.DataFrame({
    'Category': ['A', 'B', 'C'],
    'Value': [10, 20, 30]
})

# Create a bar chart using matplotlib
plt.bar(df['Category'], df['Value'])
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')

# Show the chart
plt.show()
