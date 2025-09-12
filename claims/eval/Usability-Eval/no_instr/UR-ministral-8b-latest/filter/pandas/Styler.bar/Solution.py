import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data_dict = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 30, 40]
}

# Create DataFrame
df = pd.DataFrame(data_dict)

# Plot bar chart
df.plot(x='Category', y='Values', kind='bar', color='blue')

# Fill the background with custom color
plt.axhspan(ymin=0, ymax=df['Values'].max()+1, color='lightblue', alpha=0.5)

# Display the chart
plt.show()
