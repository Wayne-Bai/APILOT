import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Assuming you have a DataFrame called df with categorical features
df = pd.DataFrame({
    'color': ['red', 'green', 'blue', 'red', 'blue'],
    'shape': ['circle', 'square', 'circle', 'square', 'circle']
})

# Initialize OneHotEncoder
encoder = OneHotEncoder()

# Fit and transform the categorical features
encoded_features = encoder.fit_transform(df[['color', 'shape']]).toarray()

# Convert to a DataFrame
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(['color', 'shape']))

# Append encoded features to the original DataFrame
final_df = pd.concat([df, encoded_df], axis=1)

print(final_df)
