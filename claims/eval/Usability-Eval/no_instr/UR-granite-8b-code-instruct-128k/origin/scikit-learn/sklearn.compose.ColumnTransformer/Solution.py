# Import the necessary libraries
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Create a sample DataFrame
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
df = pd.DataFrame(data)

# Apply StandardScaler to 'col1' and 'col3'
scaler = StandardScaler()
df[['col1', 'col3']] = scaler.fit_transform(df[['col1', 'col3']])

# Print the transformed DataFrame
print(df)
