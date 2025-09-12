
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

# Sample data
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Define transformers
transformers = [('scaler', StandardScaler(), ['A', 'B'])]

# Apply transformers to columns of DataFrame
ct = ColumnTransformer(transformers, remainder='passthrough')
transformed_data = ct.fit_transform(df)

# Display the transformed data
print(transformed_data)
