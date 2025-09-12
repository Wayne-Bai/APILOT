import pandas as pd

# Assuming you have a DataFrame 'df' with a column 'codes'
df = pd.DataFrame({
    'codes': ['A', 'B', 'C', 'A', 'B', 'C']
})

# Convert 'codes' column to categorical type
df['codes'] = df['codes'].astype('category')

# Print the DataFrame
print(df)
