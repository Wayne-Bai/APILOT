import pandas as pd

# Assuming df is your original DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Reset the index
df_reset = df.reset_index(drop=True)

print(df_reset)
