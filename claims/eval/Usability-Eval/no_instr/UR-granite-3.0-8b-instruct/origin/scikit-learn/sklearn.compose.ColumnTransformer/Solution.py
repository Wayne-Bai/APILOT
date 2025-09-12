from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Assuming df is your DataFrame and you want to apply OneHotEncoder to 'categorical_column' and StandardScaler to 'numerical_column'

# Initialize the transformers
categorical_transformer = OneHotEncoder(handle_unknown='ignore')
numerical_transformer = StandardScaler()

# Initialize the ColumnTransformer
ct = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, ['categorical_column']),
        ('num', numerical_transformer, ['numerical_column'])
    ])

# Apply the transformers to the DataFrame
df_transformed = ct.fit_transform(df)
