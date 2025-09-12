# importing necessary libraries
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd

# assuming df is the DataFrame you provided
# df = pandas DataFrame

# create column transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), [0, 1]),
        ('cat', OneHotEncoder(), [2])
    ]
)

# fit and transform the data
df_processed = preprocessor.fit_transform(df)

# convert back to DataFrame
df_processed = pd.DataFrame(df_processed)
