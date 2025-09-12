import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Example DataFrame
data = {
    'age': [25, 30, 35, 40, 45],
    'sex': ['male', 'female', 'female', 'male', 'male'],
    'income': [50000, 60000, 70000, 80000, 90000]
}
df = pd.DataFrame(data)

# Define a ColumnTransformer to apply different transformations to different columns
transformer = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['age', 'income']), # Standard scaling for numeric data
        ('cat', OneHotEncoder(), ['sex'])             # One-hot encoding for categorical data
    ],
    remainder='passthrough' # This argument specifies what to do with columns not explicitly selected
)

# Apply the transformers
transformed_data = transformer.fit_transform(df)

# Print the transformed data
print(transformed_data)
