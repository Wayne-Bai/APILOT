import pandas as pd

# Sample data
data = {
    'City': ['Chicago', 'Chicago', 'Chicago', 'Boston', 'Boston', 'Boston'],
    'Year': [2020, 2021, 2022, 2020, 2021, 2022],
    'Sales': [100, 200, 300, 400, 500, 600],
    'Expenses': [50, 75, 100, 150, 200, 250]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Stack the prescribed level(s) from columns to index
# Here, we are stacking 'Year' level from columns to index
df_stacked = df.set_index(['City', 'Year']).stack().unstack(1)

# Rename the columns for better understanding
df_stacked.columns = ['Sales', 'Expenses']

# Print the resulting DataFrame
print("\nResulting DataFrame after stacking 'Year' level:")
print(df_stacked)
