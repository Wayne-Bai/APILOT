
import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': ['apple', 'banana', 'cherry'],
    'C': [4.5, 6.3, 7.8]
}
df = pd.DataFrame(data)

# Convert the DataFrame to a dictionary
df_dict = df.to_dict(orient='records')

print(df_dict)
