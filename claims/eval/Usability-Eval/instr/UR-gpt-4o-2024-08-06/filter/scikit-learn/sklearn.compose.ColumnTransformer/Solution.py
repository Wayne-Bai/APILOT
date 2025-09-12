import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_selector, make_column_transformer
from sklearn.pipeline import Pipeline

# Sample DataFrame
data = {
    'age': [29, 35, 42, 27],
    'salary': [20000, 32000, 25000, 22000],
    'city': ['New York', 'San Francisco', 'Los Angeles', 'San Francisco']
}
df = pd.DataFrame(data)

# Define the transformers
numerical_transformer = StandardScaler()
categorical_transformer = OneHotEncoder()

# Create column selectors
numerical_selector = make_column_selector(dtype_include=['int64', 'float64'])
categorical_selector = make_column_selector(dtype_include=object)

# Create the ColumnTransformer
preprocessor = make_column_transformer(
    (numerical_transformer, numerical_selector),
    (categorical_transformer, categorical_selector)
)

# Transform the dataset
df_transformed = preprocessor.fit_transform(df)

# Convert the result to a DataFrame for easier interpretation
df_transformed = pd.DataFrame(df_transformed, columns=['age_scaled', 'salary_scaled', 'city_New York', 'city_San Francisco', 'city_Los Angeles'])

print(df_transformed)
