import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Convert DataFrame to dictionary
dict_data = df.to_dict()

print(dict_data)
