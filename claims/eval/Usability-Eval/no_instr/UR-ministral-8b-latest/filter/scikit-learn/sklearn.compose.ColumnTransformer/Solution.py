import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np

# Sample DataFrame
data = {
    'A': np.random.rand(100),
    'B': np.random.rand(100),
    'C': np.random.randint(0, 100, size=100)
}
df = pd.DataFrame(data)

# Define the columns to apply transformers
numeric_cols = ['A', 'B']
categorical_cols = ['C']

# Initialize transformers
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler()) # StandardScaler scales the numeric columns
])

# Combine transformers in a ColumnTransformer object
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_cols)
    ],
    remainder='passthrough'  # for automatic transformation of remaining columns
)

# Apply the transformers to the DataFrame
transformed_df = preprocessor.fit_transform(df[numeric_cols])

# Display the transformed DataFrame
print(transformed_df)
