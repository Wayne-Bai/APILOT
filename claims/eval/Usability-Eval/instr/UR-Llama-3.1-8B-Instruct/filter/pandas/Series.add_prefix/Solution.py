import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave'],
    'Age': [25, 30, 35, 40],
    'Country': ['USA', 'UK', 'Australia', 'Germany']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Prefixing labels with a string
prefix = 'Country_'
df['Country_Prefix'] = df['Country'].apply(lambda x: prefix + x)

# Renaming the original 'Country' column
df = df.rename(columns={'Country': 'Country_Original'})

print("\nDataFrame after prefixing and renaming:")
print(df)
