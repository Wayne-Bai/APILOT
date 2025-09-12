import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data)

# Reset the index of the DataFrame
df_reset = df.reset_index(drop=True)
print(df_reset)
