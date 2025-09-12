import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# create a sample dataframe with categorical columns
data = {'category_1': ['a', 'b', 'c'], 
        'category_2': ['d', 'e', 'f']}
df = pd.DataFrame(data)

# one-hot encode the categorical columns
encoder = OneHotEncoder(categories='auto')
one_hot_encoded_df = encoder.fit_transform(df[['category_1', 'category_2']])

# view the one-hot encoded dataframe
print(one_hot_encoded_df)
