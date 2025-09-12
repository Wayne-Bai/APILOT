# Import pandas library
import pandas as pd

# Define a function to calculate the quantile
def calculate_quantile(df, column_name, quantile_value):
    """
    Calculate the quantile of a given column in a DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.
        column_name (str): Name of the column to calculate the quantile.
        quantile_value (float): Quantile value between 0 and 1.

    Returns:
        float: The calculated quantile.
    """
    return df.groupby('category')[column_name].apply(lambda x: pd.Series.sort_values(x).iloc[int(len(x) * quantile_value)])

# Create a sample DataFrame
data = {
    'category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'values': [10, 20, 30, 40, 50, 60, 70, 80, 90]
}
df = pd.DataFrame(data)

# Calculate the 50th percentile (median) of the 'values' column for each category
result = calculate_quantile(df, 'values', 0.5)
print(result)
