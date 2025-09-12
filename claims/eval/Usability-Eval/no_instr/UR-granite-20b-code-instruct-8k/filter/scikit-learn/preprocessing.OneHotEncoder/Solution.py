
import sklearn
from sklearn.preprocessing import OneHotEncoder

# Assuming you have a pandas DataFrame df with a categorical column 'column_name'

# Create an instance of OneHotEncoder
onehot_encoder = OneHotEncoder(sparse=False)

# Fit and transform the DataFrame 'column_name'
onehot = onehot_encoder.fit_transform(df[['column_name']])

# Convert the one-hot array to a DataFrame
df_onehot = pd.DataFrame(onehot, columns=onehot_encoder.get_feature_names(['column_name']))

# Concatenate the original DataFrame with the one-hot DataFrame
df = pd.concat([df, df_onehot], axis=1)

# Drop the original categorical column
df = df.drop('column_name', axis=1)
