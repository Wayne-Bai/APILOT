import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Let's create a simple pandas dataframe
raw_data = {'name': ['Kelly', 'Jessica', 'John', 'Anne', 'Frank'],
            'age': [30, 25, 45, 33, 54],
            'city': ['New York', 'Los Angeles', 'San Francisco', 'Chicago', 'Atlanta'],
            'income': [50000, 65000, 80000, 90000, 45000]}
df = pd.DataFrame(raw_data)

# Let's suppose 'age' and 'income' are numerical columns that we want to standardize
numeric_features = ['age', 'income']
numeric_transformer = StandardScaler()

# And 'city' is a categorical column that we want to one-hot encode
categorical_features = ['city']
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

# Now let's create the ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])

# Now we can fit_transform our preprocessor to the dataframe
df[numeric_features + categorical_features] = preprocessor.fit_transform(df[numeric_features + categorical_features])

print(df)
