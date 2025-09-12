import pandas as pd

def group_quantile(df, group_by, quantile):
    # Calculate the quantile for each group
    quantiles = df.groupby(group_by).apply(lambda x: x.quantile(quantile))

    # Flatten the DataFrame to get the quantile values
    quantile_values = quantiles.stack().reset_index()

    # Rename the columns
    quantile_values.columns = ['Group', 'Quantile']

    return quantile_values
