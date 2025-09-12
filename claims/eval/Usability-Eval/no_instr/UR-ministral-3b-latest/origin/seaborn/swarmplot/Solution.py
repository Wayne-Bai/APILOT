import seaborn as sns

# Sample data creation
import pandas as pd
import numpy as np

data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': np.random.rand(10, 4)
}
df = pd.DataFrame(data)

# Melt the DataFrame to create a long format DataFrame
df_melted = df.melt(id_vars=['Category'], var_name='variant', value_name='Value')

# Plot the categorical scatter plot
sns.scatterplot(data=df_melted, x="Category", y="Value", hue='variant')
