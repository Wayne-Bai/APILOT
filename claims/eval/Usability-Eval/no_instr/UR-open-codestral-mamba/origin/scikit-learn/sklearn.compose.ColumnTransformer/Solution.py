import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Data for a dummy example
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
df = pd.DataFrame(data)

# Specify the transformations for each column
transformers = [('standardize', StandardScaler(), ['col1', 'col2', 'col3'])]

# Build preprocessing pipeline
pipeline = Pipeline(transformers)

# Apply transformations
preprocessed_data = pipeline.fit_transform(df)

# Convert back to dataframe
preprocessed_data_df = pd.DataFrame(preprocessed_data, columns=df.columns)

preprocessed_data_df
