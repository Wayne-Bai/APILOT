import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Sample DataFrame
data = {
    'numerical_col': [1, 2, 3, 4, 5],
    'categorical_col': ['A', 'B', 'A', 'C', 'B']
}
df = pd.DataFrame(data)

# Define the transformers
numerical_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

# Specify the columns for each transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, ['numerical_col']),
        ('cat', categorical_transformer, ['categorical_col'])
    ])

# Create a pipeline with the preprocessor
pipeline = Pipeline(steps=[('preprocessor', preprocessor)])

# Apply the transformers to the DataFrame
transformed_data = pipeline.fit_transform(df)

# If you want to convert the transformed data back to a DataFrame
transformed_df = pd.DataFrame(transformed_data)

print(transformed_df)
