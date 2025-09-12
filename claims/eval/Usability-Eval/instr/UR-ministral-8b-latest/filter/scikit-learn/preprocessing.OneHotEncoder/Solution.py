import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Sample data
data = pd.DataFrame({
    'Feature1': ['A', 'B', 'A', 'C', 'B'],
    'Feature2': ['X', 'Y', 'Y', 'X', 'Z']
})

# Instructions
one_hot_encoder = OneHotEncoder(sparse=False)

# Fit and transform categorical features
one_hot_encoded = one_hot_encoder.fit_transform(data)

# Convert to DataFrame
one_hot_encoded_df = pd.DataFrame(one_hot_encoded)

# Renaming columns (optional)
one_hot_encoded_df.columns = one_hot_encoder.get_feature_names_out(data.columns)

print(one_hot_encoded_df)
