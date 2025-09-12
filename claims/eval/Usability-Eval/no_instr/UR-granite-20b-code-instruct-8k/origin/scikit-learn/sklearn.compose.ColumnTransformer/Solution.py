from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Define the transformers to be applied to each column
transformers = [
    ('scaler', StandardScaler(), ['column1', 'column2']),  # Apply StandardScaler to columns 'column1' and 'column2'
    ('onehot', OneHotEncoder(), ['column3'])  # Apply OneHotEncoder to column 'column3'
]

# Create a ColumnTransformer object with the defined transformers
ct = ColumnTransformer(transformers)

# Apply the transformers to the input data (X)
X_transformed = ct.fit_transform(X)
