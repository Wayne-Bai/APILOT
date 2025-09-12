from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pandas as pd

# Assuming df is your DataFrame and it has columns 'cat', 'num', and 'text'
# 'cat' is a categorical column, 'num' is a numerical column, and 'text' is a text column

# Define the transformers for each column
categorical_transformer = OneHotEncoder(handle_unknown='ignore')
numerical_transformer = StandardScaler()
text_transformer = TfidfVectorizer()

# Define the column transformers
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, ['cat']),
        ('num', numerical_transformer, ['num']),
        ('text', text_transformer, ['text'])
    ])

# Apply the transformers to the DataFrame
df_transformed = preprocessor.fit_transform(df)
