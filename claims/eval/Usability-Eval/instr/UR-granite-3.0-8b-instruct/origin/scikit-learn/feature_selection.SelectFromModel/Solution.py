from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Assuming X is your feature matrix and y is your target variable
# X = ...
# y = ...

# Define the transformer for numerical features
num_transformer = Pipeline(steps=[
    ('scaler', StandardScaler()),
    ('selector', SelectKBest(score_func=f_classif, k=5))
])

# Define the transformer for categorical features (if any)
cat_transformer = Pipeline(steps=[
    ('selector', SelectKBest(score_func=f_classif, k=5))
])

# Combine the transformers
preprocessor = ColumnTransformer(
    transformers=[
        ('num', num_transformer, ['numeric_column1', 'numeric_column2']),
        ('cat', cat_transformer, ['categorical_column1', 'categorical_column2'])
    ])

# Define the model
model = RandomForestClassifier()

# Define the meta-transformer
meta_transformer = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', model)
])
