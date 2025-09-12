# Import necessary libraries from scikit-learn (version 1.1 onwards)
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Import necessary libraries for building the example dataset
import pandas as pd
import numpy as np

# Building a sample dataframe with categorical and numerical features
data = {
    'Color': ['Red', 'Green', 'Blue', 'Red', 'Green', 'Blue'],
    'Size': ['Small', 'Medium', 'Large', 'Small', 'Medium', 'Large'],
    'Quantity': [1, 2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)

# Define a ColumnTransformer to apply the MultiLabelBinarizer to categorical data
numeric_features = ['Quantity']
categorical_features = ['Color', 'Size']
preprocessor = ColumnTransformer(
    transformers=[
        (numeric_features, None, numeric_features),
        (categorical_features, MultiLabelBinarizer(), categorical_features)
    ]
)

# Create a pipeline with the preprocessor
pipe = Pipeline([("Preprocessor", preprocessor)])

# Transform the dataframe using the pipeline
transformed_data = pipe.fit_transform(df)

# Print the original and transformed dataframes
print("Original Dataframe:")
print(df)
print("\nTransformed Dataframe:")
print(transformed_data.toarray())
