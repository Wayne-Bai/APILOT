import pandas as pd
# Load data into a pandas DataFrame
data = {'Column1': [1, 2, 3], 'Column2': [4, 5, 6], 'Column3': [7, 8, 9]}
df = pd.DataFrame(data)
# Hide the column headers
df.columns = pd.Index([])
# Print the DataFrame
print(df)
