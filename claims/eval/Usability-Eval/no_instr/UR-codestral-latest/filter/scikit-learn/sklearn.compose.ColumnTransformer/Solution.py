# Importing necessary libraries
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd

# Assuming df is your DataFrame and it has numerical columns 'num_col1', 'num_col2' and categorical column 'cat_col'

# Define the transformers
numerical_transformer = StandardScaler()
categorical_transformer = OneHotEncoder()

# Combining transformers
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, ['num_col1', 'num_col2']),
        ('cat', categorical_transformer, ['cat_col'])])

# Apply the transformations to the DataFrame
df_transformed = preprocessor.fit_transform(df)
