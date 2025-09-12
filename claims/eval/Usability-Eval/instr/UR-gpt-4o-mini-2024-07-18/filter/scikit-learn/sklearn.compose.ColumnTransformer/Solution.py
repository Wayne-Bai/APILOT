from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd

# Sample DataFrame
data = {
    'numerical_feature_1': [1.0, 2.0, 3.0],
    'numerical_feature_2': [4.0, 5.0, 6.0],
    'categorical_feature': ['A', 'B', 'A']
}
df = pd.DataFrame(data)

# Define the column transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['numerical_feature_1', 'numerical_feature_2']),
        ('cat', OneHotEncoder(), ['categorical_feature'])
    ]
)

# Applying the transformers to the DataFrame
transformed_data = preprocessor.fit_transform(df)

print(transformed_data)
