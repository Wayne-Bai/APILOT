import pandas as pd

def resample_time_series(data, rule):
    """
    Resamples time-series data using pandas.

    Parameters:
        data (pd.DataFrame): DataFrame containing time series data with 'timestamp' column.
        rule (str): The resampling rule, e.g., 'W-MON', 'M', '1D', 'H', etc.

    Returns:
        pd.Series: Resampled time series data.
    """
    # Ensure the 'timestamp' column is of datetime type
    data['timestamp'] = pd.to_datetime(data['timestamp'])

    # Set the 'timestamp' column as the index
    data.set_index('timestamp', inplace=True)

    # Resample the data
    resampled_data = data.resample(rule).sum()

    return resampled_data

# Example usage:
# data = pd.DataFrame({
#     'timestamp': pd.date_range(start='2021-01-01', periods=10, freq='D'),
#     'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# })
# resampled_data = resample_time_series(data, 'W')
# print(resampled_data)
