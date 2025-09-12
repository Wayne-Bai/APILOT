# Importing the pandas library
import pandas as pd
import numpy as np

# Create a numpy array with 3 dimensions
data = np.arange(27).reshape(3, 3, 3)

# Create a pandas Series
series = pd.Series(data)

# Create a pandas DataFrame
df = pd.DataFrame({
    'A' : [1, 2, 3],
    'B' : [4, 5, 6],
    'C' : [7, 8, 9],
})

# Create a pandas Panel
panel = pd.Panel(np.arange(27).reshape(3, 3, 3), items=['Item1', 'Item2', 'Item3'],
                 major_axis=['A', 'B', 'C'], minor_axis=['X', 'Y', 'Z'])

# Return the elements in the given positional indices along an axis for series
print("Return elements of series by indices")
print(series.take([0, 1]))

# Return the elements in the given positional indices along an axis for dataframe
print("\nReturn elements of dataframe by indices")
print(df.take(indices=[0, 1], axis=0))

# Return the elements in the given positional indices along an axis for panel
print("\nReturn elements of panel by indices")
print(panel.take(items=[0, 2]))
