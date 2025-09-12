# Import the necessary libraries
from sklearn.base import BaseEstimator
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

# Create a DataFrame
df = pd.DataFrame({
    'A': ['cat', 'dog', 'cat', 'bird'],
    'B': [1, 2, 3, 4],
    'C': ['no', 'yes', 'no', 'yes']
})

# Define categorical and numerical columns
categorical_cols = ['A', 'C']
numerical_cols = ['B']

# Create a pipeline for numerical columns (in this case, no transformation is applied)
numerical_transformer = Pipeline(steps=[
    ('normalize', BaseEstimator())  # Replace normalize with your transformer
])

# Create a pipeline for categorical columns
categorical_transformer = Pipeline(steps=[
    ('encoder', OneHotEncoder(handle_unknown=' informatio  n'))
])

# Combine the pipelines and configure the preprocessing for categorical and numerical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ]
)

# Define a pipeline that includes the preprocessing step
clf = Pipeline(steps=[('preprocessor', preprocessor),
                     ('classifier', BaseEstimator())  # Replace with your classifier
])

# Train the model
X = df.drop('B', axis=1)  # X does not need to have a target variable
y = df['B']  # Target variable
clf.fit(X, y)

print(clf.predict(X))
