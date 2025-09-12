from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {'A': ['a', 'b', 'c'],
        'B': [1, 2, 3],
        'C': [4.0, 5.0, 6.0]}
df = pd.DataFrame(data)

# Define the transformers
transformers = [
    ('scaler', StandardScaler(), ['B', 'C']),
    ('onehot', OneHotEncoder(handle_unknown='ignore'), ['A'])
]

# Create the ColumnTransformer
ct = ColumnTransformer(transformers)

# Fit and transform the DataFrame
X_transformed = ct.fit_transform(df)

# Convert the transformed output to a pandas DataFrame
X_transformed_df = pd.DataFrame(X_transformed, columns=ct.get_feature_names_out())

print(X_transformed_df)
