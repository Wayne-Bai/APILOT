import pandas as pd

def calculate_standard_error_of_mean(dataframe, group_column, value_column):
    # Group the data by the specified column
    grouped = dataframe.groupby(group_column)[value_column]
    
    # Compute the standard error of the mean for each group, excluding missing values
    standard_error = grouped.std() / (grouped.count() ** 0.5)
    
    return standard_error
