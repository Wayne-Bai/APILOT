import pandas as pd

# Create a DataFrame
data = {'Name': ['Tom', 'Nick', 'John'],
        'Age': [20, 21, 19]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Map values using input mapping or function
def map_values(x):
    if x > 20:
        return 'Adult'
    else:
        return 'Teenager'

df['Age Group'] = df['Age'].apply(map_values)

print("\nDataFrame after mapping values:")
print(df)
