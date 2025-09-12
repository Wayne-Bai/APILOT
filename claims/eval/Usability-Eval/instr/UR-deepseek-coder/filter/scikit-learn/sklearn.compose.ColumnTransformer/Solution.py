import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_transformer

# Sample DataFrame
data = {
    'numerical_column': [1, 2, 3, 4, 5],
    'categorical_column': ['A', 'B', 'A', 'C', 'B']
}
df = pd.DataFrame(data)

# Define the transformers
numerical_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(sparse=False)

# Apply transformers to columns
preprocessor = make_column_transformer(
    (numerical_transformer, ['numerical_column']),
    (categorical_transformer, ['categorical_column'])
)

# Fit and transform the data
transformed_data = preprocessor.fit_transform(df)

# Convert the transformed data back to a DataFrame for better visualization
transformed_df = pd.DataFrame(transformed_data, columns=preprocessor.get_feature_names_out())

print(transformed_df)
