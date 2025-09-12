from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd
import numpy as np

# Example data
data = {
    'numeric_feature': [1.0, 2.0, 3.0, 4.0],
    'categorical_feature': ['cat', 'dog', 'cat', 'bird']
}
df = pd.DataFrame(data)

# Define which transformations to apply to which columns
transformers = [
    ('num', StandardScaler(), ['numeric_feature']),        # Numeric transformation
    ('cat', OneHotEncoder(), ['categorical_feature'])      # Categorical transformation
]

# Create the ColumnTransformer
column_transformer = ColumnTransformer(transformers)

# Fit and transform the data
transformed_data = column_transformer.fit_transform(df)

# Print the transformed data
print(transformed_data)
