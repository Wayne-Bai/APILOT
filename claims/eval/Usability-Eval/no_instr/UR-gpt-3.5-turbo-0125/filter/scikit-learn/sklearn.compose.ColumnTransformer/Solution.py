
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

# Assuming we have a pandas DataFrame 'data' with columns to be transformed

# Define the columns to be scaled
columns_to_scale = ['column1', 'column2']

# Create the ColumnTransformer
ct = ColumnTransformer(
    transformers=[
        ('scaler', StandardScaler(), columns_to_scale)
    ],
    remainder='passthrough'  # Pass through columns not specified for scaling
)

# Fit and transform the data
data_transformed = ct.fit_transform(data)

# Convert the transformed data back to a pandas DataFrame
data_transformed = pd.DataFrame(data_transformed, columns=columns_to_scale + data.columns[len(columns_to_scale):])
