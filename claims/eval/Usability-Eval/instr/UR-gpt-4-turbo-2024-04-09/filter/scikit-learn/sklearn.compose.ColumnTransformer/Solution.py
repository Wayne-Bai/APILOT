import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Example DataFrame
data = {
    'age': [25, 35, 45, 55],
    'salary': [50000, 60000, 70000, 80000],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Create a ColumnTransformer to apply different preprocessing to different columns
ct = ColumnTransformer(
    transformers=[
        ('scaler', StandardScaler(), ['age', 'salary']),  # Apply standard scaling to the numeric columns
        ('encoder', OneHotEncoder(), ['city'])  # Apply one-hot encoding to the categorical column
    ],
    remainder='passthrough'  # Specifies that the remaining columns should be kept without changes
)

# Fit and transform the data
transformed_data = ct.fit_transform(df)
print(transformed_data)
