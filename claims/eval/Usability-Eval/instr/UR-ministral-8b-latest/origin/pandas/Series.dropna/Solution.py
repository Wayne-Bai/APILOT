import pandas as pd

# Assume we have the following DataFrame
data = {
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, None, 3, 4]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Fill missing values with a specific strategy
df_filled = df.fillna(df.mean())

# Display the DataFrame after filling missing values
print("\nDataFrame after filling missing values:")
print(df_filled)
