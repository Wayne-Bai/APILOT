import pandas as pd

# Sample data in the form of a list
data = ["Index1", "Index2", "Index3", "Index4", "Index5"]

# Creating a pandas Series to represent the data
series = pd.Series(data)

# Converting the Series to an array
array = series.values

array
