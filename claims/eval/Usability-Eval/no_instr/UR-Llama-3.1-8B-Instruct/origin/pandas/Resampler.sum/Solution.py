# Import the pandas library
import pandas as pd

# Create a DataFrame
data = {
    'City': ['New York', 'New York', 'Chicago', 'Chicago', 'Los Angeles', 'Los Angeles'],
    'Year': [2020, 2021, 2020, 2021, 2020, 2021],
    'Sales': [100, 200, 50, 75, 300, 250]
}

df = pd.DataFrame(data)

# Group by City and Year, and compute the sum of Sales
grouped_df = df.groupby(['City', 'Year'])['Sales'].sum().reset_index()

# Print the result
print(grouped_df)
