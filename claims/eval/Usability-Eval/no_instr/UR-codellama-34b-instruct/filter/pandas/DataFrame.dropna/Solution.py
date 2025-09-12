import pandas as pd

# Create a sample DataFrame with missing values
df = pd.DataFrame({'Name': ['John', 'Amy', np.nan],
                   'Age': [25, 30, np.nan]})

# Remove rows that contain missing values
df.dropna(inplace=True)

print(df)
