import pandas as pd

def index_of_min_series(s):
    """
    Return index of first occurrence of minimum over requested axis for pandas Series
    """
    ser = s.copy()  # Create a copy to avoid altering the original series
    return ser.idxmin()

def index_of_min_dataframe(df):
    """
    Return index of first occurrence of minimum over requested axis for pandas DataFrame
    """
    return df.stack().idxmin()

# Create a sample pandas Series
s = pd.Series([5, 2, 9, 1])
print(index_of_min_series(s))

# Create a sample pandas DataFrame
df = pd.DataFrame({
    'A': [5, 2, 9, 1],
    'B': [3, 6, 7, 4]
})
print(index_of_min_dataframe(df))
