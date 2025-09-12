# Import necessary libraries. We are using pandas for data manipulation, 
# numpy for numerical operations, and scikit-learn for imputation.
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Create a sample DataFrame with missing values.
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)

# Define feature and target (X and y)
X = df

# Fill missing values with mean of the respective column
imputer_mean = SimpleImputer(strategy='mean')
# Or with median
imputer_median = SimpleImputer(strategy='median')
# Or with most frequent value
imputer_most_frequent = SimpleImputer(strategy='most_frequent')
# Or with a constant value
imputer_constant = SimpleImputer(strategy='constant', fill_value=0)

# To use these imputers on our DataFrame X, we first need to prep our DataFrame for use with these imputers.
numerical_features = X.select_dtypes(include=['int64', 'float64']).columns

# Use ColumnTransformer to impute missing values selectively (e.g., numeric values only)
numeric_transformer = Pipeline(steps=[
    ('imputer', imputer_mean),
# Or with median
# ('imputer', imputer_median),
# Or with most frequent value
# ('imputer', imputer_most_frequent),
# Or with a constant value, set the fill_value to'mean''median''most_frequent' as needed 
# Remember that'most_frequent' will ignore NaN, and 'constant' will fill all values
])

# Combine only numeric features
preprocessor = ColumnTransformer(
    transformers=[('num', numeric_transformer, numerical_features)],
)

# Now we fit and transform our preprocessor.
X = preprocessor.fit_transform(X)

# Print the resulting DataFrame
print(X)
