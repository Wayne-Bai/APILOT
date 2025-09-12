from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pandas as pd

# Sample DataFrame
data = {
    'numeric_feature': [1, 2, 3, 4, 5],
    'categorical_feature': ['A', 'B', 'A', 'B', 'A']
}

df = pd.DataFrame(data)

# Define the transformers for different columns
# Scale numeric features and one-hot encode categorical features
column_transformer = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['numeric_feature']),
        ('cat', OneHotEncoder(), ['categorical_feature'])
    ]
)

# Apply the transformations
transformed_data = column_transformer.fit_transform(df)

# Convert to DataFrame for easier understanding
transformed_df = pd.DataFrame(transformed_data)
print(transformed_df)
