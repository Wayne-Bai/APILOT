import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 24, 19, 31]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Draw a bar chart
df.set_index('Category').plot(kind='bar')

plt.title('Bar Chart Example')
plt.xlabel('Category')
plt.ylabel('Values')
plt.grid(True)

plt.show()
