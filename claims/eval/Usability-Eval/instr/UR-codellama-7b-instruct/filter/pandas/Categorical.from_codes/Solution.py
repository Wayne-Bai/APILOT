
import pandas as pd

# Define the data
codes = ['A', 'B', 'C']
categories = ['apple', 'banana', 'orange']

# Create a categorical variable
categorical_variable = pd.Series(categories, index=codes)
