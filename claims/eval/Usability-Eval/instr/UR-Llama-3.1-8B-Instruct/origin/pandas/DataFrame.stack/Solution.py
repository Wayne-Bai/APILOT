# Import the required library
import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Location': ['NYC', 'LAX', 'SFO', 'MIA', 'ORD'],
    'Level1': [10, 20, 30, 40, 50],
    'Level2': [100, 200, 300, 400, 500]  # prescribed level
}

# Create a DataFrame
df = pd.DataFrame(data)

# Stack the 'Level1' and 'Level2' columns to a multi-indexed Series
stacked_series = pd.Series({
    'Level1': ['Level1_1', 'Level1_2', 'Level1_3', 'Level1_4', 'Level1_5'],
    'Level2': ['Level2_1', 'Level2_2', 'Level2_3', 'Level2_4', 'Level2_5']
}, index=['Level1', 'Level2'])

# Use reset_index and melt to pivot the data
pivoted_df = stacked_series.reset_index().melt(var_name='Levels', value_name='Values')

# Print the resulting DataFrame
print(pivoted_df)
