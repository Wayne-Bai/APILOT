import pandas as pd

# Example DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

df = pd.DataFrame(data)

# Convert the DataFrame to a dictionary
df_dict = df.to_dict()

print(df_dict)
