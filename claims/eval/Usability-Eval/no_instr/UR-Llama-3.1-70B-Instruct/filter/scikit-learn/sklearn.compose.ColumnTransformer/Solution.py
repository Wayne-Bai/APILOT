# Import necessary libraries
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np

# Create a sample dataset
data = {
    'Age': [25, 26, 27, 28, np.nan],
    'Country': ['USA', 'Canada', 'Germany', 'UK', 'France'],
    'Score': [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

# Define which columns to apply transformation
numeric_features = ['Age']
categorical_features = ['Country']

# Create a numeric transformer
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),  
    ('scaler', StandardScaler())])

# Create a categorical transformer
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

# Use ColumnTransformer to combine the numeric and categorical transformers
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])

# Fit the preprocessor to the data and transform the data
preprocessor.fit(df)
transformed_data = preprocessor.transform(df)

# Print the transformed data
print(transformed_data)
