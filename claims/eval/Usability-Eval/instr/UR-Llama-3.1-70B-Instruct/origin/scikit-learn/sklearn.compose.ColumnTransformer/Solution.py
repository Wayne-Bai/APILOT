# Import necessary libraries from scikit-learn
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd
import numpy as np

# Generate sample data
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': ['cat', 'dog', 'cat', np.nan, 'dog'],
    'C': [10.0, np.nan, 30.0, 40.0, np.nan]
}
df = pd.DataFrame(data)

# Create preprocessing operations for numeric and categorical features
numeric_features = ['A', 'C']
categorical_features = ['B']

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),  # handle missing numeric values
    ('scaler', StandardScaler())  # scale numeric features
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),  # handle missing categorical values
    ('onehot', OneHotEncoder(handle_unknown='ignore'))  # one-hot encode categorical features
])

# Use ColumnTransformer to combine the preprocessing operations
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# Fit the preprocessor to the data and transform it
preprocessor.fit(df)
transformed_data = preprocessor.transform(df)

print(transformed_data)
